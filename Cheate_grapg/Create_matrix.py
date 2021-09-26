from typing import List, Optional
from  DataCSV.GetDataCSV import get_days_list
import matplotlib.colors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

CVC_PATH = r'C:\Users\mosco\PycharmProjects\Team2\DataCSV\data500.csv'


def get_day_lists(day_num, csv_path):
    data = pd.read_csv(csv_path)
    data_day = (data[data.record == day_num]).reset_index()
    del data_day['index']
    list_x = data_day['latitude'].tolist()
    list_y = data_day['longitude'].tolist()
    list_speed = data_day['velocity'].tolist()
    label = data_day['sure_tral'][0]
    return [list_x, list_y, list_speed, day_num, label]

#
# arr = get_day_lists(21 , CVC_PATH  )
    
def make_some_lists(arr):
    print(arr)
    x = list(map(lambda x: x * 1000000, arr[0]))
    print(x)
    y = list(map(lambda x: x * 1000000, arr[1]))
    print(y)
    dx = []
    dy = []
    tmpx = 0
    tmpy = 0
    # for i in range(len(x)):
    #     dx.append((tmpx-x[i])*40000*math.cos((tmpx+x[i])*math.pi/360)/360)
    #     tmpx = x[i]
    #     dy.append((tmpy-y[i])*40000/360)
    #     tmpy = y[i]
    # dx = (lon1-lon2)*40000*math.cos((lat1+lat2)*math.pi/360)/360
    # dy = (lat1-lat2)*40000/360

    # x = dx[::]
    # y = dy[::]

    tempx = x[0]
    tempy = y[0]

    for i in range(1, len(x)):
        x[i] = x[i] + tempx
        tempx = x[i]
        y[i] = y[i] + tempy
        tempy = y[i]
    
    print(x)
    print(y)
    
    x = list(map(lambda x: round(x, 2), x))
    y = list(map(lambda x: round(x, 2), y))
    
    new_x = []
    for i in range(1, len(x)):
        delt = (x[i] + x[i - 1]) / 100
        for j in range(0, 100):
            new_x.append(x[i] + j * delt)
    
    new_y = []
    for i in range(1, len(x)):
        delt = (y[i] + y[i - 1]) / 100
        for j in range(0, 100):
            new_y.append(y[i] + j * delt)
    
    speed = arr[2]
    max_speed = max(speed)
    speed = list(map(lambda x: x / max_speed, speed))
    new_speed = []
    for i in range(1, len(speed)):
        for j in range(100):
            new_speed.append(speed[i])
    
    print(new_speed)
    
    speed = np.array(new_speed)
    color = np.array([new_speed, new_speed, new_speed])
    color = np.transpose(color)
    return [x,y,color]


def create_picture(x: Optional[List[float]], y: Optional[List[float]], color: Optional[List[float]]  , lable , day_num):
    fig, axes = plt.subplots()
    # print(type(fig))
    for i in range(1, len(x) - 1):
        plt.plot(x[i - 1:i + 1], y[i - 1:i + 1], c=matplotlib.colors.to_rgb(color[i - 1]) , linewidth = 4)

    axes.set_facecolor('#afeded')
    # plt.axis('off')

    fig.set_figwidth(16)  # ширина и
    fig.set_figheight(16)  # высота "Figure"
    # temp = str(day_num) +'_' + str(lable)
    # fig.savefig(temp + '.png')
    plt.show()
    return fig
    # pass
#
# lists = get_days_list(CVC_PATH)
# for i in lists:
#
#     temp = get_day_lists(i , CVC_PATH)
#
#     create_picture(*make_some_lists(temp[0:3]) , temp[4] ,temp[3])
