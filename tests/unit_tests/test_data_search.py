"""
search_id
- spaces
- gene_id in str format only? (how many numbers?)
- letters inside?
- no geneid record?


search_symbol
- all caps
- all small caps
- spaces
- input fakegene
- all numbers?

search_gene
- HGNC:1101ID search works
- BRCA2Symbol search work
- br afFinds BRAF
- @@@@Invalid input
- ""Invalid input
"""


import pytest
from pathlib import Path
from typing import List, Dict

from hgnc_gene_data_collector.models import data_search

