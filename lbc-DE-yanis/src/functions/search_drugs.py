# from functions.ingestion import *
from functions.merging import *


# Search mentioned drugs

def get_drugs():
    drugs = read_files()[0]
    drugs_list = drugs['drug'].tolist()
    return drugs_list


def find_drug_mentions(df):
    drug_mapping = []
    for drug in get_drugs():
        journal_mention = df[df.apply(lambda column: column.str.contains(drug, case=False, na=False)).any(axis=1)][
            'journal'].tolist()
        date_mention = df[df.apply(lambda column: column.str.contains(drug, case=False, na=False)).any(axis=1)][
            'date'].tolist()
        drug_mapping.append([drug, journal_mention, date_mention])
    df = pd.DataFrame(drug_mapping, columns=['drug_name', 'journal', 'date'])
    df = df.set_index(['drug_name']).apply(pd.Series.explode).reset_index()
    return df
