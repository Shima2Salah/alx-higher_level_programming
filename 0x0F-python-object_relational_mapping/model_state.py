#!/usr/bin/python3
"""create table contain states"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """class contains states information"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
