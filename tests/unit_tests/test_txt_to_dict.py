"""
- file path not found?
- file not found?
- no gene record?
- no symbol/ hgnc id/name/prev symbol/prev name/alias symbol/
alias name/maneselect/refseq accession
- len(gene record) not 9?


File exists?
File missing?
TSV readable?
"""

import pytest
from pathlib import Path
from typing import List, Dict
import csv

from hgnc_gene_data_collector.models import convert_txt_to_dict , create_gene_record,

# ------------------------------------------------------------------
# parse_line tests
# ------------------------------------------------------------------

def test_create_gene_record():
    """ Test creation of gene record from row """
    row = {
        "symbol": "BRCA2",
        "hgnc_id": "HGNC:1101",
        "name": "BRCA2",
        "prev_symbol": "",
        "prev_name": "",
        "alias_symbol": "",
        "alias_name": "",
        "mane_select": "",
        "refseq_accession": "",
    }
    result = create_gene_record(row)
    assert result["Alias Gene Symbol"] == []

def test_empty_values_become_empty_lists():

    row = {
        "symbol": "BRCA2",
        "hgnc_id": "HGNC:1101",
        "name": "BRCA2 DNA repair associated",
        "prev_symbol": "",
        "prev_name": "",
        "alias_symbol": "",
        "alias_name": "",
        "mane_select": "",
        "refseq_accession": "",
    }

    result = create_gene_record(row)

    assert result["Previous Gene Symbol"] == []
    assert result["Previous Gene Name"] == []
    assert result["Alias Gene Symbol"] == []
    assert result["Alias Gene Name"] == []
    assert result["MANE Select transcript"] == []
    assert result["RefSeq accessions"] == []


def test_multiple_values_are_split():

    row = {
        "symbol": "BRCA2",
        "hgnc_id": "HGNC:1101",
        "name": "BRCA2 DNA repair associated",
        "prev_symbol": "AAA|BBB|CCC",
        "prev_name": "",
        "alias_symbol": "XXX|YYY",
        "alias_name": "",
        "mane_select": "",
        "refseq_accession": "",
    }

    result = create_gene_record(row)

    assert result["Previous Gene Symbol"] == ["AAA", "BBB", "CCC"]
    assert result["Alias Gene Symbol"] == ["XXX", "YYY"]

def test_required_fields_are_mapped():

    row = {
        "symbol": "BRCA2",
        "hgnc_id": "HGNC:1101",
        "name": "BRCA2 DNA repair associated",
        "prev_symbol": "",
        "prev_name": "",
        "alias_symbol": "",
        "alias_name": "",
        "mane_select": "",
        "refseq_accession": "",
    }

    result = create_gene_record(row)

    assert result["HGNC gene symbol"] == "BRCA2"
    assert result["HGNC ID"] == "HGNC:1101"
    assert result["Gene Name"] == "BRCA2 DNA repair associated"


def test_convert_txt_to_dict_returns_dataset(tmp_path):

test_file = tmp_path / "test.tsv"
test_file.write_text(
"symbol\thgnc_id\tname\tprev_symbol\tprev_name\talias_symbol\talias_name\tmane_select\trefseq_accession\n"
"BRCA2\tHGNC:1101\tBRCA2\t\t\t\t\t\t\n"
)

result = convert_txt_to_dict(test_file)

assert isinstance(result, list)
assert len(result) == 1
assert result[0]["HGNC gene symbol"] == "BRCA2"


def test_convert_txt_to_dict_missing_file():

with pytest.raises(FileNotFoundError):
convert_txt_to_dict("does_not_exist.tsv")

def test_convert_txt_to_dict_empty_file(tmp_path):

    test_file = tmp_path / "empty.tsv"
    test_file.write_text("")

    result = convert_txt_to_dict(test_file)

    assert result == []


