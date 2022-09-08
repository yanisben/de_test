from utils.configs import *
from functions.ingestion import *
from functions.merging import *
import pandas as pd

# configs = Configs()


#  Normalization of dates

def normalize_dates(df):
    df['date'] = pd.to_datetime(df['date'])
    df = df.astype(dtype='string')
    return df
