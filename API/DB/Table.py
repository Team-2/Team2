import sqlalchemy.orm
from sqlalchemy import Column, String, Integer, Float, ForeignKey

from Start_DB import Base


class Ships(Base):
    __tablename__ = 'ships'

    name_ship = Column(Integer, primary_key=True)
    record_day = Column(Integer, nullable=False)
    forecast = Column(Float, nullable=True)


class Records(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True)
    record_id = Column(Integer, ForeignKey('ships.record_day'))
    ships = sqlalchemy.orm.relationship("Ships", backref='records')
    time = Column(String)
    lan = Column(Float)
    lat = Column(Float)
    speed = Column(Float)
    angle = Column(Float)
