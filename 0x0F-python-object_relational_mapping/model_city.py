#!/usr/bin/python3

from model_state import Base, State
from sqlalchemy import Column, String, Integer
from sqlalchemy import ForeignKey


class City(Base):
    """City class"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('State.id'), nullable=False)