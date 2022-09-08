from utils.configs import Configs

configs = Configs()


# Outputs to a json file


def df_to_json(df):
    df.to_json(configs.JSON_RESULT_PATH, orient='records', indent=3, index=True, force_ascii=False)
    print(f'Data pipeline executed, check output here : {configs.JSON_RESULT_PATH}')
