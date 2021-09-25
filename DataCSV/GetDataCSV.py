import pandas as pd
import numpy as np


def get_one_day(csv_path, num_day):
    # todo return pd.data для 1 дня
    data = pd.read_csv(csv_path)
    data_day = (data[data.record == num_day].drop(['ship', 'record'], axis=1)).reset_index()
    del data_day['index']
    return data_day


def get_days_list(csv_path):
    #
    #
    data = pd.read_csv(csv_path)
    days = list(set(np.array(data.record)))
    return days


CVC_PATH = r'C:\Users\mosco\PycharmProjects\Team2\DataCSV\data500.csv'

#
# print(get_days_list(CVC_PATH))
# for i in get_one_day(CVC_PATH , 1):
#     print(i , end= '  ')
# for i in get_one_day(CVC_PATH , 1).get_values():
#     print(list(map(float , i)))
# print(get_one_day(CVC_PATH , 1))
