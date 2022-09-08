from functions.adhocquery import *
from functions.ingestion import read_json_output


class Adhoc:

    @staticmethod
    def launch():
        df = read_json_output()
        return f"The journal that mentions the most drugs is : {get_journal_with_most_distinct_drug_mentions(df)}"
