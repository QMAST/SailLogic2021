# coding=utf-8

from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = 'localhost:5432'
db_name = 'sail_logic'
db_user = 'postgres'
db_password = 'Sa1lL0gic'
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)

Base = declarative_base()

# TODO we only need one superclass, its hacky having three
class Entity():
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)

    def __init__(self, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by

class CommandEntity():
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)
    commandID = Column(String)
    commandValue = Column(String)
    
    def __init__(self, created_by, commandID, commandValue):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by
        self.commandID = commandID
        self.commandValue = commandValue

#TODO figure out list of sensors
class ExistingStateEntity():
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)
    
    def __init__(self, created_by, commandID, commandValue):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by