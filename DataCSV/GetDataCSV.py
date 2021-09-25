import pandas as pd
import  numpy as np

def get_one_day(csv_path, num_day):
    # todo return pd.data для 1 дня
    data = pd.read_csv(csv_path)
    data_day = (data[data.record == num_day].drop(['Unnamed: 0', 'ship', 'record'], axis=1))
    return data_day


def get_days_list(csv_path):
    # todo return List(days_num)
    data = pd.read_csv(csv_path)
    days = list(set(np.array(data.record)))
    return days
