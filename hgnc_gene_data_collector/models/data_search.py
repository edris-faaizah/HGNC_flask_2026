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
from typing import Any, Optional #to find out type
logger = logging.getLogger(__name__)



def search_by_ID(gene_id: str,lightweight_gene_dataset: list[dict[str, Any]],) -> Optional[dict[str, Any]]:
    """Search for a gene record by HGNC ID."""
    logger.info("Searching for HGNC ID: %s", gene_id)

    for record in lightweight_gene_dataset:
        if record["HGNC ID"] == gene_id:
            logger.info("Gene record found for HGNC ID: %s", gene_id)
            gene_record = record
            return gene_record

    logger.warning("No gene record found for HGNC ID: %s", gene_id)
    return None


def search_by_symbol(gene_symbol: str,lightweight_gene_dataset: list[dict[str, Any]]) -> Optional[dict[str, Any]]:
    """Search for a gene record by gene symbol."""
    logger.info("Searching for gene symbol: %s", gene_symbol)

    for record in lightweight_gene_dataset:
        if record["HGNC gene symbol"] == gene_symbol:
            logger.info("Gene record found for symbol: %s", gene_symbol)
            gene_record = record
            return gene_record

    logger.warning("No gene record found for symbol: %s", gene_symbol)
    return None


def search_gene(request_input: str,dataset: list[dict[str, Any]]) -> Optional[dict[str, Any]]:
    """Search by HGNC ID or gene symbol."""
    request_input = "".join(request_input.strip().split()).upper()

    if request_input.startswith("HGNC:"):
        return search_by_ID(request_input, dataset)

    if request_input.isalnum():
        return search_by_symbol(request_input, dataset)

    logger.warning("Invalid input format: %s", request_input)
    return None