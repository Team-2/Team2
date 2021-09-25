from API.DB.Start_DB import session , Days , Records





def get_id( record_id : int):
    return session.query(Records).filter(record_id == Records.record_day).first().id