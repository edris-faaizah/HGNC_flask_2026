"""
Dataset search module
-----------------
PURPOSE
-----------------
This module includes the function to search the lightweight dataset for a specific gene record
based on input.

Input:
- Gene symbol
- HGNC ID

Output:
- Gene record dictionary if found, else None

"""

import logging
logger = logging.getLogger(__name__)
from hgnc_gene_data_collector.models.txt_to_dict import convert_txt_to_dict

def search_by_ID(gene_id):
    """
    Search for a gene record in the lightweight_dataset by HGNC ID.

    Input:
        gene_id (str): The HGNC ID to search for. in specific format HGNC:XXXXX

    Returns:
        dict or None: The gene record dictionary if found, else None.
    """
    logger.info("Searching for gene record with HGNC ID: %s", gene_id)

    for record in lightweight_gene_dataset:
        if record["HGNC ID"] == gene_id:
            logger.info("Gene record found for HGNC ID: %s", gene_id)
            gene_record = record
            return gene_record
    else:
        logger.warning("No gene record found for HGNC ID: %s", gene_id)
        return None

def search_by_symbol(gene_symbol):
    """
    Search for a gene record in the lightweight_dataset by HGNC gene symbol.

    Input:
        gene_symbol (str): The HGNC gene symbol to search for.
    
    Returns:
        dict or None: The gene record dictionary if found, else None.
    """
    logger.info("Searching for gene record with HGNC gene symbol: %s", gene_symbol)
    for record in lightweight_gene_dataset:
        if record["HGNC gene symbol"] == gene_symbol:
            logger.info("Gene record found for HGNC gene symbol: %s", gene_symbol)
            gene_record = record
            return gene_record
    else:
        logger.warning("No gene record found for HGNC gene symbol: %s", gene_symbol)
        return None



def search_gene(request_input):
    """
    Search for a gene record in the lightweight_dataset based on the input. 
    """
    request_input = "".join(request_input.strip().split()).upper()

    if request_input.startswith("HGNC:"):
        return search_by_ID(request_input)
    if not request_input.startswith("HGNC:") and request_input.isalnum():
            return search_by_symbol(request_input)
    else:
        logger.warning("Invalid input format: %s", request_input)
        return None
    
lightweight_gene_dataset = convert_txt_to_dict()
request_input = input("Enter HGNC gene symbol or HGNC ID (e.g., HGNC:12345): ")
print(search_gene(request_input))

