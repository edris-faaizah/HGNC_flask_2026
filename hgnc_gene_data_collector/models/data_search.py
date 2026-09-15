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
from models.txt_to_dict import lightweight_gene_dataset

def search_by_ID(gene_id):
    """
    Search for a gene record in the lightweight_dataset by HGNC ID.

    Input:
        gene_id (str): The HGNC ID to search for. in specific format HGNC: XXXXX

    Returns:
        dict or None: The gene record dictionary if found, else None.
    """
    logger.info("Searching for gene record with HGNC ID: %s", gene_id)
    for record in lightweight_gene_dataset:
        if record["HGNC_ID"] == 
    
    
    gene_record = next((record for record in lightweight_gene_dataset if record["HGNC ID"] == gene_id), None)
    
    if gene_record:
        logger.info("Gene record found for HGNC ID: %s", gene_id)
    else:
        logger.warning("No gene record found for HGNC ID: %s", gene_id)
    
    return gene_record


def search_gene(request_input):
    if request_input.startswith("HGNC"):
        gene_record = lightweight_gene_dataset.get(request_input) # cant use this cause this is fr dict when my lightweight dataset is list of dict
        return gene_record
    return None

