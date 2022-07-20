import argparse
import yaml
import pandas as pd
from skleran.model_selection import train_test_split

def split_data(config_path):
    config = read_params(config_path)
    test_data_path =   ['split_data']['test_path'] 
    train_data_path = ['split_data']['train_path']
    split_ratio =    ['split_data']['test_size']
    random_state =  ['base']['random_state']
    raw_data_path = ['load_data']['raw_dataset_csv']
    df = pd.read_csv(raw_data_path)
    train, test = train_test_split(df,random_state=random_state, test_size= split_ratio)

    train.to_csv(train_data_path, index = False)
    test.to_csv('test_data_path',index = False)


if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    split_data(config_path=parsed_args.config)