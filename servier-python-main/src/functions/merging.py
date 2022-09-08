from functions.ingestion import read_files
import pandas as pd

# Merge datasets


def merge_pubmed():
    pubmed_csv = read_files()[2]
    pubmed_json = read_files()[3]
    pubmed_merged = pd.concat([pubmed_csv, pubmed_json], ignore_index=True)
    return pubmed_merged


def merge_all():
    pubmed_df = merge_pubmed()
    clinical_df = read_files()[1]
    clinical_df = clinical_df.rename(columns={"scientific_title": "title"})
    merged = pd.concat([pubmed_df, clinical_df], ignore_index=True)
    return merged
