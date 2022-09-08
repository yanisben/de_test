# from functions.ingestion import *
from functions.merging import *


# Search mentioned drugs

def get_drugs():
    drugs = read_files()[0]
    drugs_list = drugs['drug'].tolist()
    return drugs_list


def find_drug_mentions(df):
    drugs = get_drugs()
    results = []
    df = df.select_dtypes(include=["string"])
    for drug in drugs:
        contains_in_journal = df[df.apply(lambda column: column.str.contains(drug, regex=True, case=False, na=False)).any(axis=1)]['journal'].tolist()
        contains_in_dates = df[df.apply(lambda column: column.str.contains(drug, regex=True, case=False, na=False)).any(axis=1)]['date'].tolist()
        results.append([drug, contains_in_journal, contains_in_dates])
    df = pd.DataFrame(results, columns=['drug_name', 'journal', 'date'])
    df = df.set_index(['drug_name']).apply(pd.Series.explode).reset_index()
    return df
