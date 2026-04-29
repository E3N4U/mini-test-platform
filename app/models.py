from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class API(Base):
    __tablename__ = "apis"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    url = Column(String)
    method = Column(String)


class TestCase(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)
    api_id = Column(Integer, ForeignKey("apis.id"))
    input_data = Column(Text)
    expected = Column(Text)

    api = relationship("API")