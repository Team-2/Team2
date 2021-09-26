from typing import List
from Start_DB import session
from AI.Plug import NN
import numpy as np
from DataCSV.GetDataCSV import get_one_day, get_days_list
from Start_DB import Records, Days, delete_DB, Base, engine
from Security.CodeData import some_encryption, some_decryption
from GLOBAL import CVC_PATH
# CVC_PATH = r'C:\Users\mosco\PycharmProjects\Team2\DataCSV\data500.csv'
from AI.NeironNetwork import make_pred

def get_result(path) -> dict:
    predict = make_pred(path)
    return predict


def update_db(CVC_PATH):
    days = get_days_list(CVC_PATH)
    result = []
    predict_dict = get_result(CVC_PATH)
    for i in days:
        temp_list = []
        temp = Records(record_day=int(i), prediction=predict_dict[i])
        for j in get_one_day(CVC_PATH, i).get_values():
            j = list(map(float, j))
            temp_list.append(Days(time=j[5], lan=j[1], lat=j[0], speed=j[3], angle=int(j[2]), seconds=int(j[7])))
        temp.days = temp_list
        result.append(some_encryption(temp))

    session.add_all(result)
    session.commit()


delete_DB()

Base.metadata.create_all(bind=engine)
update_db(CVC_PATH)
