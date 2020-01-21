#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    """id = Column(String(60), nullable=False, primary_key=True)"""
    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref="state")

    @property
    def cities(self):
        objs = models.storage.all()
        alist = []
        for key, value in objs.items():
            if "City" in key and getattr(value, 'state_id') == self.id:
                alist.append(value)

        return alist
