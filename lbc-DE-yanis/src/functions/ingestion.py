from utils.configs import *
from functions.normalization import *
import pandas as pd

# configs = Configs()

# Read input datasets


def read_files():
    drugs_csv = pd.read_csv(DRUGS_PATH)
    clinical_csv = normalize_dates(pd.read_csv(CLINICAL_TRIALS_PATH))
    pubmed_csv = normalize_dates(pd.read_csv(PUBMED_CSV_PATH))
    pubmed_json = normalize_dates(pd.read_json(PUBMED_JSON_PATH))

    return drugs_csv, clinical_csv, pubmed_csv, pubmed_json


def read_json_output():
    pubmed_json = normalize_dates(pd.read_json(JSON_RESULT_PATH))
    return pubmed_json
