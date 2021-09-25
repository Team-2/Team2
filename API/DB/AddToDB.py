from DataCSV.GetDataCSV import get_one_day ,  get_days_list
from typing import List





def update_db(days : List[int] , csv_path ):



    for i in days:
        result = get_one_day(csv_path , i)
