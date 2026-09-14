import csv

with open("hgnc_data/hgnc_complete_set.txt", mode="r" , newline="", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter="\t")
    lightweight_gene_dataset = [] # dict of all gene records.
    for row in csv_reader:
        gene_record = { #to limit each gene with only record i am interested in
            "HGNC gene symbol":row["symbol"] or None, #because single value, can be empty
            "HGNC ID":row["hgnc_id"] or None,
            "Gene Name":row["name"] or None,
            "Previous Gene Symbol":[] if not row["prev_symbol"] else row["prev_symbol"].split("|"), #because can have multile values
            "Previous Gene Name":[] if not row["prev_name"] else row["prev_name"].split("|"),
            "Alias Gene Symbol":[] if not row["alias_symbol"] else row["alias_symbol"].split("|"),
            "Alias Gene Name":[] if not row["alias_name"] else row["alias_name"].split("|") ,
            "MANE Select transcript":[] if not row["mane_select"] else row["mane_select"].split("|"),
            "RefSeq accessions":[] if not row["refseq_accession"] else row["refseq_accession"].split("|"), #added this to try and find mane trasncripts if any
        }
        lightweight_gene_dataset.append(gene_record) # combine all gene record into one dict
    print(lightweight_gene_dataset[10000]) # check the first record to see if it is correct
