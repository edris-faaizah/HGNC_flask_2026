# HGNC_flaskproject_2026_edris

## HGNC Gene Information Web Application

This is a Software Engineering Assessment Project for STP Year One Bioinformatics Tutorials. This project is designed to provide clinical scientist with a simple web application to find information about human genes from data provided by the HUGO Gene Nomenclature Committee (HGNC).

Users enter a HGNC-approved gene symbol (for example, `BRCA2`) or HGNC ID (for example, `1101`) and the application displays the corresponding:

- HGNC gene symbol
- HGNC ID
- Gene name
- Previous gene symbols
- Previous gene names
- Gene aliases/synonyms
- MANE Select transcript
- MANE Plus Clinical transcript(s)

---

## Data Source

The application uses locally stored copy of HGNC complete dataset in tab-separated (TSV) format.

File name: hgnc_complete_set.txt

Download URL: https://storage.googleapis.com/public-download-files/hgnc/tsv/tsv/hgnc_complete_set.txt 

The source dataset is maintained by HGNC and is updated regularly. This means that the exact contents of the dataset may change depending on when you download or when it is updated.

However for this project, dataset has been stored locally: 

| Folder | File name |
|------|--------|
| hgnc_data| hgnc_complete_set.txt |

### Dataset used for development and testing:

- Source: HGNC_complete_set.txt 
- Length: 16944473 (16M) [text/plain]
- Downloaded: 2026-08-18 13:56:16
- SHA256: 4ad72ffc6bca0d0858bb7234cfb3c7b1fb10e8e693e2f8d5c0842b4cfb03e748

If you would like to use the latest version of the dataset:
- either remove local dataset
- or rename dataset accordingly
- ensure the dataset path configured in the application is updated accordingly.
- application is designed to run one dataset at a time

To download latest dataset, while in directory `~/HGNC_flask_2026/hgnc_data` , on your terminal:

```bash
wget -O hgnc_complete_set.txt \
https://storage.googleapis.com/public-download-files/hgnc/tsv/tsv/hgnc_complete_set.txt
```

For reproducibility purpose, you can record metadata in README.md (example shown above):
- Source
- Length
- Downloaded Date and Time
- SHA256*

*to run SHA256:
```bash
sha256sum hgnc_complete_set.txt
```

If the dataset filename changes, update the `DATA_FILE` setting in `settings.py` accordingly.

---

## Project Architecture

This project is intentionally lightweight and is intended as an assignment project. Unlike larger Flask projects, the application does not use a database or ORM. Instead, the selected dataset is loaded into memory during application startup and all searches are performed against in-memory data.

The request flow is as follows:

```text
Browser
▼
Flask routes
▼
View Functions
▼
Model Layer ( tsv data access)
▼
Jinja Template
▼
Browser
```

---

## Installation

This project uses a fully controlled and reproducible Conda environment

### 1. Create the Conda environment

```bash
conda env create -f environment.yml
```

### 2. Activate the environment

```bash
conda activate HGNCgenedata
```

### 3. Install the project

```bash
pip install -e .
```

The editable installation allows changes made to the source code to be immediately reflected without reinstalling the package.

---

## Running the application

Start the Flask development server with:

```bash
python -m hgnc_gene_data_collector.app
```

Alternatively, the application can be run directly from the source file:

```bash
python hgnc_gene_data_collector/app.py
```

The application will be available at:
```text
http:// (find out the url)
```

---

## Testing

Run the complete unit and UI test suite:

```bash
pytest
```

Run the test suite with coverage:

```bash
pytest \
    --cov=hgnc_gene_data_collector \
    --cov-report=term-missing:skip-covered \
    --cov-report=html \
    --cov-report=xml
```

An interactive HTML coverage report is generated in:

```text
htmlcov/index.html
```

## Shutting down

Stop the flask development server using:

```text
Ctrl+C
```

Deactivate the Conda environment when finished:

```bash
conda deactivate
```

---

## Notes on reproducibility

This project is intended for clinical and educational use and therefore prioritises reproducibility.

- The Conda environment fixes the Python interpreter version.
- All Python dependencies are pinned.
- Installation is deterministic across systems.
- Templates and static assets are packaged with the application.
- The complete test suite can be executed using pytest to verify correct installation and behaviour.


- include in test on using more than one dataset? needed or not cause i put that optional download for new dataset