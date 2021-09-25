from flask import Blueprint
from flask import jsonify, make_response
from DB.Start_DB import session
# from Answerer.answerer import Answerer

ship = Blueprint('ship', __name__)

# Этот запрос нужен для получения координат и времени для построения графика
@ship.route('/mfcs/<string:name_record>', methods=['GET'])
def get_data(name_record: str):
    ship_name, record_day = map(int, name_record.split('_'))
    # todo return all pair ([x,y] , time )

    result = []
    return make_response(jsonify(result))


# Этот запрос вернет все пары (ship_name , record_name) для который параметр forecast
# больше опред значения

@ship.route('/mfcs/all', methods=['GET'])
def get_list_pair():
    # for ind in df.index:
    #     para=(df['ship'][ind],df["record"][ind])
    #     try:
    #         freq_dict[para]+=1
    #     except KeyError:
    #         freq_dict[para]=1
    temp = session.query()
    pass
