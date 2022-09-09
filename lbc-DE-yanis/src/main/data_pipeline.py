from functions.search_drugs import *
from functions.df_to_json import *
from functions.merging import *


class DataPipeline:

    # Launches data pipeline

    @staticmethod
    def launch():
        df = merge_all()
        search_df = find_drug_mentions(df)
        return df_to_json(search_df)


if __name__ == "__main__":
    pipeline = DataPipeline()
    pipeline.launch()
