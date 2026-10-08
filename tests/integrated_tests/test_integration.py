import pytest
from pathlib import Path
from typing import List, Dict
import csv

from hgnc_gene_data_collector.models.data_search import search_by_ID , search_by_symbol, search_gene

from hgnc_gene_data_collector.models.txt_to_dict import convert_txt_to_dict , create_gene_record


@pytest.fixture #since i am reusing dataset
def test_sample_file(tmp_path):
    test_file = tmp_path / "test_hgnc.txt" #example of DATA FILE path

    test_file.write_text(
        "hgnc_id\tsymbol\tname\tprev_symbol\tprev_name\talias_symbol\talias_name\tmane_select\trefseq_accession\n"
        "HGNC:1\tABC1\tAlpha Beta Gamma 1\t\t\t\t\tNM_000001.1\tNM_000001\n"
        "HGNC:2\tABC2\tAlpha Beta Gamma 2\t\t\tALPHA2\t\t\tNM_000002\n"
        "HGNC:3\tABC3\tAlpha Beta Gamma 3\tOLDABC3\tOld Alpha Beta Gamma 3\tABCIII|ABC-3\tAlias ABC3\tNM_000003.1|NM_000003.2\tNM_000003\n"
        "HGNC:4\tXYZ1\tXylophone Zinc 1\t\t\t\t\tNM_000004.1\tNM_000004\n"
        "HGNC:5\tLNC1\tLong Non Coding RNA 1\tOLDLNC\tOld Long Non Coding RNA 1\tLNC-ALIAS\tLNC Alias Name\t\t\n"
    )
	
    return test_file

def test_integrated_id(test_sample_file):
    
    test_dataset = convert_txt_to_dict(test_sample_file)
    test_input = "HGNC:1"

    result = search_gene(test_input, test_dataset)

    assert result["HGNC ID"] == "HGNC:1"


def test_integrated_symbol(test_sample_file):
    
    test_dataset = convert_txt_to_dict(test_sample_file)
    test_input = "ABC3"

    result = search_gene(test_input, test_dataset)

    assert result["Previous Gene Symbol"] == ["OLDABC3"]


def test_integrated_invalid(test_sample_file):
    
    test_dataset = convert_txt_to_dict(test_sample_file)
    test_input = "$$$"

    result = search_gene(test_input, test_dataset)

    assert result is None


