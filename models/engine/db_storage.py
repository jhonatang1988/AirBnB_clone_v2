#!/usr/bin/python3
"""
DBStorage
"""
from models.base_model import Base, BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
        HBNB_ENV = os.getenv('HBNB_ENV')

        try:
            self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                          .format(HBNB_MYSQL_USER,
                                                  HBNB_MYSQL_PWD,
                                                  HBNB_MYSQL_HOST,
                                                  HBNB_MYSQL_DB),
                                          pool_pre_ping=True)
            if HBNB_ENV is 'test':
                Base.metadata.drop_all(bind=self.__engine)
        except:
            raise
            print(":(")

    def all(self, cls=None):
        obs = []
        class_list = [State, City, User, Place, Review, Amenity]
        dict_all = {}

        try:
            if cls is None:
                for tab in class_list:
                    obs.append(self.__session.query(tab).all())
                objs = [item for sublist in obs for item in sublist]

            else:
                objs = self.__session.query(eval(cls)).all()

            for obj in objs:
                    obj_id = getattr(obj, 'id')
                    key = obj.to_dict()['__class__'] + '.' + obj_id
                    dict_all[key] = obj

            return dict_all
        except:
            raise
            print(":(")

    def new(self, obj):
        try:
            self.__session.add(obj)
        except:
            raise
            print(":(")

    def save(self):
        try:
            self.__session.commit()
        except:
            raise
            print(":(")

    def delete(self, obj=None):
        try:
            if obj is not None:
                obj_id = getattr(obj, 'id')
                q = self.__session.query(type(obj).__name__)\
                                  .filter(type(obj).__name__.id == obj_id)\
                                  .first()
                self.__session.delete(q)
                self.__session.commit()
        except:
            raise
            print(":(")

    def reload(self):
        try:
            Base.metadata.create_all(self.__engine)
            Session = scoped_session(sessionmaker(bind=self.__engine,
                                                  expire_on_commit=False))
            self.__session = Session()
        except:
            raise
            print(":(")

    def close(self):
        try:
            self.__session.close()
        except:
            raise
            print(":(")
