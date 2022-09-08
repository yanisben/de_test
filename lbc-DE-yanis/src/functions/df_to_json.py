from utils.configs import *

# configs = Configs()


# Outputs to a json file


def df_to_json(df):
    df.to_json(JSON_RESULT_PATH, orient='records', indent=3, index=True, force_ascii=False)
    print(f'Data pipeline executed, check output here : {JSON_RESULT_PATH}')
