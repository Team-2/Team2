from typing import List, Optional

import matplotlib.colors
import matplotlib.pyplot as plt
import numpy as np

from API.DB.Start_DB import session, Days
from API.FuncAPI.Tools import get_id
from Security.CodeData import some_decryption


def temp():
    id_r = get_id(20)
    temp = session.query(Days).filter(Days.day_id == id_r).all()
    temp_lat = []
    temp_lan = []
    temp_sec = []
    temp_speed = []
    for i in temp:
        temp_lan.append(some_decryption(i.lan))
        temp_sec.append(some_decryption(i.speed))
        temp_lat.append(some_decryption(i.lat))
        temp_speed.append(some_decryption(i.speed))
    result = [temp_lan, temp_lat, temp_sec, temp_speed]
    # print(result)
    return result


arr = temp()
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

speed = arr[3]
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

rgb = np.random.rand(24, 3)


# print(rgb)
def asd(list_x: Optional[List[float]], list_y: Optional[List[float]], list_speed: Optional[List[float]]):
    fig, axes = plt.subplots()

    for i in range(1, len(x) - 1):
        plt.plot(x[i - 1:i + 1], y[i - 1:i + 1], c=matplotlib.colors.to_rgb(color[i - 1]))

    axes.set_facecolor('lightblue')
    plt.axis('off')

    fig.set_figwidth(16)  # ширина и
    fig.set_figheight(16)  # высота "Figure"

    plt.show()
    pass


asd([1], [1], [1])
