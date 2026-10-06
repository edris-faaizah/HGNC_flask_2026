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

valid HGNC symbol
✓ valid HGNC ID
✓ gene not found
✓ invalid input
✓ empty string
✓ whitespace input


•	a valid HGNC-approved gene symbol is entered;
•	a valid HGNC ID is entered;
•	a gene cannot be found;
•	optional information is not available;
•	no search term is supplied; or
•	invalid or unexpected input is supplied.
Results and error messages should be presented clearly to the user.

"""


import pytest
from pathlib import Path
from typing import List, Dict

from hgnc_gene_data_collector.models import data_search



