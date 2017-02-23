from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Room(Base):

    __tablename__ = 'rooms'
    id = Column(Integer, autoincrement=True, primary_key=True)
    room_name = Column(String(20))
    room_type = Column(String(20))
    capacity = Column(Integer)
    c_occupants = Column(Integer, default=0)

    def __repr__(self):
        return 'Room Name:' + self.room_name + ', Type:' + self.room_type


class Person(Base):

    __tablename__ = 'people'
    id = Column(Integer, autoincrement=True, primary_key=True)
    emp_id = Column(String(20))
    name = Column(String(20))
    job_type = Column(String(20))
    office = Column(String(20))
    living_space = Column(String(20), default='N')


def create_database(db_name='amity_db'):
    if db_name:
        db_engine = create_engine("sqlite:///" + db_name + "")
    else:
        db_engine = create_engine("sqlite:///amity_db")
    Base.metadata.create_all(db_engine)
    Base.metadata.bind = db_engine
    dbsession = sessionmaker(bind=db_engine)
    session = dbsession()
    return session
