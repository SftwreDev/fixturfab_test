from sqlalchemy import Column, Integer, String

from config.settings import Base


class PcbSpecs(Base):

    __tablename__ = "pcb_specs"

    id = Column(Integer, primary_key=True, index=True)
    pcb_information = Column(String)
    value = Column(Integer)
    notes = Column(String)


class TestPointList(Base):

    __tablename__ = "test_point_list"
    
    id = Column(Integer, primary_key=True, index=True)
    net = Column(String)
    name = Column(String)
    x_coord = Column(String)
    y_coord = Column(String)
    side = Column(String)
    type = Column(String)
    hole_size = Column(String)