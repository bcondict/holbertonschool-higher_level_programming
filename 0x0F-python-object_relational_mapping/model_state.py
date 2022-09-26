#!/usr/bin/python3
'''
First state model
'''

from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''
    First class for States
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    UniqueConstraint(id)
    name = Column(String(128), nullable=False)
