import unittest

from functions.search_drugs import *
from functions.merging import *


class DataPipelineTest(unittest.TestCase):  # Inherited from the unittest.TestCase class

    @staticmethod
    def fixture_merge_all():  # Use of a static method as a fixture to be able to use outer scope functions within
        # the test class
        return merge_all()

    @staticmethod
    def fixture_search_drugs():  # Use of a static method as a fixture to be able to use outer scope functions within
        # the test class
        df = DataPipelineTest.fixture_merge_all()
        return find_drug_mentions(df)

    # search_drugs method should return a dataframe made of the 3 following columns : 'drug_name', 'journal' and 'date'

    def test_valid_columns(self):
        df = DataPipelineTest.fixture_search_drugs()
        self.assertEqual(df.columns.values.tolist(), ['drug_name', 'journal', 'date'])

    # merge_all method should join correctly pubmed and clinical publications and return columns of type string

    def test_valid_columns_types(self):
        df = DataPipelineTest.fixture_merge_all()
        self.assertEqual(str(df['id'].dtype), 'string')
        self.assertEqual(str(df['title'].dtype), 'string')
        self.assertEqual(str(df['date'].dtype), 'string')
        self.assertEqual(str(df['journal'].dtype), 'string')

    # merge_all() should return 21 records with title name

    def test_total_number_of_titles(self):
        df = DataPipelineTest.fixture_merge_all()
        merged_title_count = df['title'].count()
        expected_drug_mention_in_title_count = 21
        self.assertEqual(merged_title_count, expected_drug_mention_in_title_count)

    # search_drugs() should return 19 records

    def test_total_number_of_drugs(self):
        df = DataPipelineTest.fixture_search_drugs()
        merged_drug_count = df['drug_name'].count()
        expected_drug_mention_count = 19
        self.assertEqual(merged_drug_count, expected_drug_mention_count)

    # Diphenhydramine should be mentioned exactly 6 times

    def test_valid_number_of_mention_for_diphenhydramine(self):
        df = DataPipelineTest.fixture_search_drugs()
        expected_drug_count = 6
        drug_name = 'DIPHENHYDRAMINE'
        df = df[df['drug_name'] == drug_name]
        df = df['drug_name'].count()
        self.assertEqual(df, expected_drug_count)

    # Glucagon should be mentioned exactly zero time, given that it is not the drug list

    def test_valid_number_of_mentions_for_glucagon(self):
        df = DataPipelineTest.fixture_search_drugs()
        expected_drug_count = 0
        drug_name = 'GLUCAGON'
        df = df[df['drug_name'] == drug_name]
        df = df['drug_name'].count()
        self.assertEqual(df, expected_drug_count)


if __name__ == "__main__":
    unittest.main()
