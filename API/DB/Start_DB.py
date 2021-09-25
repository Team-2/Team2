from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship

Base = declarative_base()

engine = create_engine('sqlite:///../../db.sqlite', echo=False)

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base.query = session.query_property()


class Records(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True)
    record_day = Column(Integer, nullable=False)
    prediction = Column(Float , nullable= False)

class Days(Base):
    __tablename__ = "days"

    id =  Column(Integer, primary_key=True)
    day_id = Column(Integer , ForeignKey('records.id'))
    records = relationship("Records" , backref = 'days')
    time = Column(Integer)
    lan = Column(Float)
    lat = Column(Float)
    speed = Column(Float)
    angle = Column(Float)
    seconds = Column(Integer)


def delete_DB():
    Base.metadata.drop_all(engine)
# delete_DB()




Base.metadata.create_all(bind=engine)
# post_MFC()

