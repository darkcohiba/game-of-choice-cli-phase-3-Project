from sqlalchemy import create_engine, desc
from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer, DateTime, ForeignKey)

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///gameData.db')

Base = declarative_base()