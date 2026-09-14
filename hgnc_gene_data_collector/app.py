from flask import Flask, request, render_template
from pathlib import Path
import logging
from typing import Dict, Any, Optional

from hgnc_gene_data_collector.data_collector import settings
from hgnc_gene_data_collector.data_collector.logger import setup_logging

#use csv.dictreader to read the file and turn it into a list of dictionaries