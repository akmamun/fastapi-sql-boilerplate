# models.py
from sqlalchemy import Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    def as_dict(self):
       return {'id': self.id, 'name': self.name}
