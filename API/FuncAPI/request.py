import io

from flask import Blueprint
from flask import Response
from flask import jsonify, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

from API.DB.Start_DB import session, Days, Records
from API.FuncAPI.Tools import get_id
from Cheate_grapg.Create_matrix import create_picture, make_some_lists
from Security.CodeData import some_encryption, some_decryption

ship = Blueprint('ship', __name__)


# # Этот запрос нужен для получения координат и времени для построения графика
# @ship.route('/ship/<int:record>', methods=['GET'])
# def get_data(record: int):
#     temp_lat = []
#     temp_lan = []
#     temp_speed = []
#     id_r = get_id(record)
#     temp = session.query(Days).filter(Days.day_id == id_r).all()
#     for i in temp:
#         temp_lan.append(some_decryption(i.lan))
#         temp_speed.append(some_decryption(i.speed))
#         temp_lat.append(some_decryption(i.lat))
#     result = [temp_lan, temp_lat, temp_speed]
#
#     return make_response(jsonify(some_encryption(result)))


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

# /<int:record>
@ship.route('/ship/graph/<int:record>/plot.png')
def show_pictuer(record):
    # record = 11
    temp_lat = []
    temp_lan = []
    temp_speed = []
    id_r = get_id(record)
    lable = session.query(Records).filter(Records.record_day == record).first().prediction
    temp = session.query(Days).filter(Days.day_id == id_r).all()
    for i in temp:
        temp_lan.append(some_decryption(i.lan))
        temp_speed.append(some_decryption(i.speed))
        temp_lat.append(some_decryption(i.lat))
    result = [temp_lan, temp_lat, temp_speed]
    result = make_some_lists(result)
    fig = create_picture(result[0], result[1], result[2], lable, result)
    # fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
