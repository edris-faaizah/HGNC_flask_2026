"""

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

from hgnc_gene_data_collector.models.data_search import search_by_ID , search_by_symbol, search_gene

@pytest.fixture #since i am reusing dataset
def sample_dataset():
    return [
        {
            "HGNC gene symbol": "ABC1",
            "HGNC ID": "HGNC:0001",
            "Gene Name": "ABC1",
            "MANE Select transcript": ["NM_001234.5"],
        },
        {
            "HGNC gene symbol": "ABC2",
            "HGNC ID": "HGNC:0002",
            "Gene Name": "ABC2",
            "MANE Select transcript": [],
        },
        {
            "HGNC gene symbol": "ABC3",
            "HGNC ID": "HGNC:0003",
            "Gene Name": "ABC3",
            "MANE Select transcript": ["NM_002345.6"],
        }
    ]

#happy path testing
def test_search_by_ID_happy(sample_dataset):

    test_gene_id = "HGNC:0001"
    test_result_happy = search_by_ID(test_gene_id, sample_dataset)
    assert test_result_happy["HGNC gene symbol"] == "ABC1"


def test_search_by_symbol_happy(sample_dataset):

    test_gene_symbol = "ABC3"
    test_result_happy = search_by_symbol(test_gene_symbol, sample_dataset)
    assert test_result_happy["HGNC ID"] == "HGNC:0003"


def test_search_gene_use_ID(sample_dataset):

    test_input_01 = "HGNC:0002"
    test_input_result_01 = search_gene(test_input_01, sample_dataset)
    assert test_input_result_01["MANE Select transcript"] == []
    
    test_input_02 = "HGNC:0003"
    test_input_result_02 = search_gene(test_input_02, sample_dataset)
    assert test_input_result_02["MANE Select transcript"] == ["NM_002345.6"]

def test_search_gene_use_symbol(sample_dataset):

    test_input = "ABC1"
    test_input_result = search_gene(test_input, sample_dataset)
    assert test_input_result["MANE Select transcript"] == ["NM_001234.5"]

def test_search_gene_lowercase_input(sample_dataset):
    test_input_01 = "hgnc:0001"
    test_input_result_01 = search_gene(test_input_01, sample_dataset)
    assert test_input_result_01["MANE Select transcript"] == ["NM_001234.5"]
    test_input_02 = "abc3"
    test_input_result_02 = search_gene(test_input_02, sample_dataset)
    assert test_input_result_02["Gene Name"] == "ABC3"


def test_search_gene_removes_space(sample_dataset):

    test_input_01 = " hgnc:0001 "
    test_input_result_01 = search_gene(test_input_01, sample_dataset)
    assert test_input_result_01["MANE Select transcript"] == ["NM_001234.5"]
    test_input_02 = "abc 3"
    test_input_result_02 = search_gene(test_input_02, sample_dataset)
    assert test_input_result_02["Gene Name"] == "ABC3"


def test_search_gene_invalid_hgnc_format(sample_dataset):
    result = search_gene("hgnc_0001", sample_dataset)
    assert result is None


def test_search_gene_invalid_characters(sample_dataset):
    result = search_gene("$$$$", sample_dataset)
    assert result is None


def test_search_gene_not_found(sample_dataset):
    result = search_gene("ABC99", sample_dataset)
    assert result is None


#test for logger??