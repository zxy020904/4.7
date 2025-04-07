import requests
import os
import sklearn
import pandas as pd
from static import PREDICTOR_COLUMNS, TARGET_COLUMN

df = pd.read_csv('bots_vs_users.csv')
#替换其中的unknown值和空值
df.fillna(99, inplace=True)
df.replace('Unknown', 99, inplace=True)




def load_train_test_datasets():
    train_x, test_x, train_y, test_y = sklearn.model_selection.train_test_split(
        df[PREDICTOR_COLUMNS], df[TARGET_COLUMN], test_size=0.2, random_state=5963)
    return train_x, train_y, test_x, test_y