#!/usr/bin/python3
"""create table contain cities"""
from model_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """class contains states information"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, Foreignkey('states.id'), nullable=False)
