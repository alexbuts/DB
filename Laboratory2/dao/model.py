from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()


class ormHoliday(Base):
    __tablename__ = 'Holiday'

    holiday_name = Column(String(20), primary_key=True)
    season_year = Column(String(20), nullable=False)

    clients_ = relationship('ormClient')


class ormClient(Base):
    __tablename__ = 'Client'
    passport_num = Column(Integer, primary_key=True)
    holiday_name = Column(String(20),ForeignKey('Holiday.holiday_name') , nullable=False)
    present_name = Column(String(20),ForeignKey('Presents.present_name') ,nullable=False)
    name = Column(String(40))
    family_state = Column(String(30))
    age = Column(Integer)
    gender = Column(String(40))




class ormPresents(Base):
    __tablename__ = 'Presents'

    present_name = Column(String(20), primary_key=True)
    store_name = Column(String(30))
    count_items = Column(Integer)

    clients__ = relationship('ormClient')


