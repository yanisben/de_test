import unittest

from functions.adhocquery import *
from functions.merging import *
from functions.search_drugs import find_drug_mentions


class UsageTest(unittest.TestCase):  # Inherited from the unittest.TestCase class

    @staticmethod
    def merge_all():  # Use of a static method as a fixture to be able to use outer scope functions within
        # the test class
        return merge_all()

    @staticmethod
    def find_drug_mentions():  # Use of a static method as a fixture to be able to use outer scope functions within
        # the test class
        df = UsageTest.merge_all()
        return find_drug_mentions(df)

    @staticmethod
    def get_journal_with_most_distinct_drug_mentions():  # Use of a static method as a fixture to be able to
        # use outer scope functions within the test class
        df = UsageTest.find_drug_mentions()
        return get_journal_with_most_distinct_drug_mentions(df)

    # get_journal_with_most_distinct_mentions method should select the drug with the most mentions

    def test_adoc_query(self):
        result = UsageTest.get_journal_with_most_distinct_drug_mentions()
        expected_result = 'The journal of maternal-fetal & neonatal medicine'
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()

