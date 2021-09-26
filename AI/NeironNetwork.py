import pickle
from datetime import datetime
import pickle
import geopy
import numpy as np
import pandas as pd
from geopy import distance
from sklearn.ensemble import RandomForestClassifier
pd.options.display.max_rows = 10000
import math


class functions_for_obrabotchic():
    ### дистанция между коорд
    def distance(row):
        coords_1 = (0, 0)
        if row['ship'] == row['next_ship']:
            coords_2 = (row['next_lat'], row['next_lon'])
        else:
            coords_2 = (0, 0)
        distance = geopy.distance.geodesic(coords_1, coords_2).m
        return distance

    ### Время в секундах
    def time_to_sec(timestring):
        try:
            pt = datetime.strptime(timestring, '%H:%M:%S')
            total_seconds = pt.second + pt.minute * 60 + pt.hour * 3600
            return total_seconds
        except:
            return 0

    ### Средняя линейная скорость
    def linear_speed(row):
        if row['ship'] == row['next_ship']:
            if row['delta_time'] != 0:
                speed = row['distance'] / row['delta_time']
            else:
                speed = 0
        else:
            speed = 0
        return abs(speed)

    def delta_time(row):
        if row['ship'] == row['next_ship'] or row['next_record'] == row['record']:
            delta = row['next_time'] - row['time_in_sec']
        else:
            delta = row['time_in_sec']
        return abs(delta)


### Path до csv файла

def obrabotchic(path_to_csv):
    data = pd.read_csv(path_to_csv)
    data = data.dropna(subset=['ship', 'record', 'time'])
    data[['course', 'velocity']] = data[['course', 'velocity']].fillna(value=0)
    data[['course', 'velocity']] = data[['course', 'velocity']].replace(np.nan, 0)
    data[['course', 'velocity']] = data[['course', 'velocity']].replace('None', 0)
    data['time_in_sec'] = data['time'].apply(lambda x: functions_for_obrabotchic.time_to_sec(x))
    data = data.sort_values(by=['ship', 'record', 'time_in_sec'])
    next_lat = data['latitude'].to_list()
    next_lon = data['longitude'].to_list()
    next_record = data['record'].to_list()
    next_record.pop(-1)
    next_lat.pop(-1)
    next_lon.pop(-1)
    next_record.insert(0, 1)
    next_lon.insert(0, 0)
    next_lat.insert(0, 0)
    data['next_record'] = next_record
    data['next_lat'] = next_lat
    data['next_lon'] = next_lon
    next_time = data['time_in_sec'].to_list()
    next_ship = data['ship'].to_list()
    next_time.pop(-1)
    next_ship.pop(-1)
    next_time.insert(0, 0)
    next_ship.insert(0, 1)
    data['next_time'] = next_time
    data['next_ship'] = next_ship
    data['distance'] = data.apply(lambda row: functions_for_obrabotchic.distance(row), axis=1)
    data['delta_time'] = data.apply(lambda row: functions_for_obrabotchic.delta_time(row), axis=1)
    data['linear_speed'] = data.apply(lambda row: functions_for_obrabotchic.linear_speed(row), axis=1)
    del data['next_lat']
    del data['next_lon']
    del data['next_ship']
    del data['next_time']
    del data['time']
    del data['next_record']
    new_angles = [0] * len(data.index)
    for i, ind in enumerate(data.index):
        base_angle = math.atan(data["latitude"][ind] / data["longitude"][ind]) * 57.2958
        bow_angle = int(data["course"][ind])
        new_angles[i] = (bow_angle - base_angle) % 360
    data.assign(angle=new_angles)
    data['latitude'] = pd.to_numeric(data['latitude'])
    data['longitude'] = pd.to_numeric(data['longitude'])
    data.to_csv('new_best_data.csv', index=False)
    return data

from GLOBAL import CVC_PATH


def make_pred(PATH):
    data = obrabotchic(PATH)

    with open('AI/RF.pd', 'rb') as f:
        rf = pickle.load(f)
    del data["ship"]
    records = sorted(list(set(data.record)))
    dfs = dict(zip(records, [data[data["record"] == i].drop(["record"], axis=1) for i in records]))
    pvreds = dict(zip(records, [rf.predict(dfs[i]) for i in records]))
    for i in records:
        pvreds[i] = list(pvreds[i]).count(1) / len(pvreds[i])
    pred_diskr = dict(zip(int(records), [1 if pvreds[i] > 0.75 else 0 for i in pvreds.keys()]))
    return pred_diskr

def make_pred_done_data():
    data = pd.read_csv(r'C:\Users\mosco\PycharmProjects\Team2\AI\new_best_data.csv')

    with open(r'C:\Users\mosco\PycharmProjects\Team2\AI\RF.pd', 'rb') as f:
        rf = pickle.load(f)
    del data["ship"]
    records = sorted(list(set(data.record)))
    dfs = dict(zip(records, [data[data["record"] == i].drop(["record"], axis=1) for i in records]))
    pvreds = dict(zip(records, [rf.predict(dfs[i]) for i in records]))
    for i in records:
        pvreds[i] = list(pvreds[i]).count(1) / len(pvreds[i])
    pred_diskr = dict(zip(int(records), [1 if pvreds[i] > 0.75 else 0 for i in pvreds.keys()]))
    return pred_diskr


print(make_pred_done_data())