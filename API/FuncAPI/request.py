from flask import Blueprint
from flask import jsonify, make_response
from API.DB.Start_DB import session, Days, Records
from API.FuncAPI.Tools import get_id
from Security.CodeData import some_encryption, some_decryption

ship = Blueprint('ship', __name__)


# Этот запрос нужен для получения координат и времени для построения графика
@ship.route('/ship/<int:record>', methods=['GET'])
def get_data(record: int):
    temp_lat = []
    temp_lan = []
    temp_sec = []
    id_r = get_id(record)
    temp = session.query(Days).filter(Days.day_id == id_r).all()
    for i in temp:
        temp_lan.append(some_decryption(i.lan))
        temp_sec.append(some_decryption(i.time))
        temp_lat.append(some_decryption(i.lat))
    result = [temp_lan, temp_lat, temp_sec]
    # print(result)
    return make_response(jsonify(some_encryption(result)))


# Этот запрос вернет все пары (ship_name , record_name) для который параметр forecast
# больше опред значения

@ship.route('/ship/all', methods=['GET'])
def get_list_pair():
    acc = 0.8
    result = []
    temp = session.query(Records).filter(Records.prediction >= acc).all()
    for i in temp:
        result.append(some_decryption(i.record_day))
    return make_response(jsonify(some_encryption(result)))
