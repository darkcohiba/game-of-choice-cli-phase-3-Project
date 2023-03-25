from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer, DateTime, ForeignKey, Boolean)
from sqlalchemy.orm import relationship, backref

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# User table
class User(Base):
    __tablename__ = 'users'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    username = Column(String())
    password = Column(String())
    score = Column(String())
    
    # 1.a ✅ Add  ForeignKey('owners.id') to owner_id
    weapon_id = Column(Integer(), ForeignKey('weapon.id'))
    
    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Username:{self.username}, " \
            + f"score: {self.score}, "\
            + f"Last Weapon: {self.weapon_id}, "

# weapon table
class Weapon(Base):
    __tablename__ = 'weapons'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    name = Column(String())
    strength = Column(Integer())
    wall_breaker = Column(Boolean())

    users = relationship('User', backref=backref('user'))

    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Weapon Name:{self.name}, " \
            + f"Weapon Strength: {self.strength}, "\
            + f"Wall Breaking Ability: {self.wall_breaker}, "

