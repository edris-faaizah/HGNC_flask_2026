"""
Text to Dictionary Converter
-----------------
PURPOSE
------------------
Converting text file into a list of dictionaries.
For this project, the HGNC data is in a text file format. Which needs converting into a dictionary
As the data is large, this module will also limit the data to only what is required. 

INPUT:
- File path
- Gene record data required: 
    - "HGNC gene symbol"
    - "HGNC ID"
    - "Gene Name"
    - "Previous Gene Symbol"
    - "Previous Gene Name"
    - "Alias Gene Symbol"
    - "Alias Gene Name"
    - "MANE Select transcript"
    - "RefSeq accessions"

OUTPUT:
- The limited data will be stored in a list of dictionaries, where each dict will represent a gene record
"""

import logging
logger = logging.getLogger(__name__)

# ive removed datset import and move it to app.py
import csv
from pathlib import Path


def create_gene_record(row: dict) -> dict:
    """
    Create a lightweight gene record from a HGNC row.
    """

    return {
        "HGNC gene symbol": row["symbol"] or None,
        "HGNC ID": row["hgnc_id"] or None,
        "Gene Name": row["name"] or None,
        "Previous Gene Symbol": []if not row["prev_symbol"] else row["prev_symbol"].split("|"),
        "Previous Gene Name": []if not row["prev_name"] else row["prev_name"].split("|"),
        "Alias Gene Symbol": []if not row["alias_symbol"] else row["alias_symbol"].split("|"),
        "Alias Gene Name": []if not row["alias_name"] else row["alias_name"].split("|"),
        "MANE Select transcript": []if not row["mane_select"] else row["mane_select"].split("|"),
        "RefSeq accessions": []if not row["refseq_accession"] else row["refseq_accession"].split("|"),
    }


def convert_txt_to_dict(file_path: str | Path) -> list[dict]:
    """
    Load HGNC TSV file and convert it into a lightweight dataset.
    """

    logger.info("Starting conversion of text dictionary...")
    if not file_path:
        logger.error("No file path provided")
        raise ValueError("No file path provided")

    if not Path(file_path).exists():
        logger.error("HGNC data file not found: %s", file_path)
        raise FileNotFoundError(f"HGNC data file not found: {file_path}")

    lightweight_gene_dataset = []

    with open(file_path, mode="r",newline="",encoding="utf-8") as csv_file:

        csv_reader = csv.DictReader(csv_file,delimiter="\t")

        logger.info("Empty dataset created, processing each row as a gene record...")

        for row in csv_reader:
            gene_record = { #to limit each gene with only record i am interested in
                "HGNC gene symbol":row["symbol"] or None, #because single value, can be empty
                "HGNC ID":row["hgnc_id"] or None,
                "Gene Name":row["name"] or None,
                "Previous Gene Symbol":[] if not row["prev_symbol"] else row["prev_symbol"].split("|"), #because can have multile values
                "Previous Gene Name":[] if not row["prev_name"] else row["prev_name"].split("|"),
                "Alias Gene Symbol":[] if not row["alias_symbol"] else row["alias_symbol"].split("|"),
                "Alias Gene Name":[] if not row["alias_name"] else row["alias_name"].split("|") ,
                "MANE Select transcript":[] if not row["mane_select"] else row["mane_select"].split("|"),
                "RefSeq accessions":[] if not row["refseq_accession"] else row["refseq_accession"].split("|"), #added this to try and find mane trasncripts if any
            }
            lightweight_gene_dataset.append(gene_record) # combine all gene record into one dict
        logger.info("Conversion complete. Lightweight dataset created with %d gene records.",
        len(lightweight_gene_dataset))
    return lightweight_gene_dataset    
    #print(lightweight_gene_dataset[10000]) # check the first record to see if it is correct
            gene_record = create_gene_record(row)
            lightweight_gene_dataset.append(gene_record)

    if not lightweight_gene_dataset:
        logger.warning("Dataset loaded but contains no records")

    logger.info("Conversion complete. Lightweight dataset created with %d gene records.",len(lightweight_gene_dataset))

    return lightweight_gene_dataset
