import argparse
from get_data import read_params, get_data
import pandas as pd

def load_data(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    new_cols = [col.replace(" ", "_") for col in df.columns]
    raw_data_path = config['load_data']['raw_data_csv']
    df.to_csv()


if __name__ == "__main__":
    args = argparse.ArgumentParser(raw_data_path, index = False, header= new_cols)
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data = load_data(config_path=parsed_args.config)