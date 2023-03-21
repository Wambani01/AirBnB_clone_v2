#!/usr/bin/python3
""" database storage management """
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker


user = os.environ.get('HBNB_MYSQL_USER')
password = os.environ.get('HBNB_MYSQL_PWD')
host = os.environ.get('HBNB_MYSQL_HOST', 'localhost')
database = os.environ.get('HBNB_MYSQL_DB')


class DBStorage():
    """ a class defining methods and attributes for the database """

    __engine = None
    __session = None

    def __init__(self):
        """ initiliazes the class """
        self.__engine = create_engine(
             f'mysql+mysqldb://{user}:{password}@{host}/{database}',
             pool_pre_ping=True
        )
        hbnd_env = os.environ.get('HBNB_ENV')
        if (hbnd_env == "test"):
            Base.metadata.drop_all(engine)

   def all(self, cls=None):

       Session = sessionmaker(bind=engine)
       self.__session = Session()
       objects = {}
       if cls is not None:
           # Query for objects of a specific class
           results = self.__session.query(cls).all()
       else:
           # Query for all types of objects
           results = []
           for cls in [User, State, City, Amenity, Place, Review]:
               results.extend(self.__session.query(cls).all()
       # Add objects to dictionary
       for obj in results:
           key = "{}.{}".format(obj.__class__.__name__, obj.id)
           objects[key] = obj

       return objects
          


      

