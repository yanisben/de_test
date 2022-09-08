

# Ad-hoc processing : from the output, find the journal who mentions the most distinct drug names


def get_journal_with_most_distinct_drug_mentions(df):
    aggregated_series = df.groupby(by=['journal'], dropna=False, as_index=None)['drug_name'].nunique()
    df = aggregated_series[aggregated_series == aggregated_series.max()]
    most_distinct_drug_mentions_list = str(df['journal'].dropna().tolist()).strip('[\'\']')
    return most_distinct_drug_mentions_list
