import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True)
    email = Column(String(250), unique=True)

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True, nullable=False)
    model = Column(String(250))
    starship_class = Column(String(250))
    length = Column(Integer)
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    liked_starship = Column(Integer, ForeignKey('liked_starships.id'))
    liked_starship_relationship = relationship("liked_tarships", uselist=False)

class Liked_Starships(Base):
    __tablename__ = 'liked_starships'
    id = Column(Integer, primary_key=True)
    starship = Column(Integer, ForeignKey('starships.id'))
    starship_relationship = relationship(Starships)
    user = Column(Integer, ForeignKey('users.id'))
    user_relationship = relationship(Users)
    
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True, nullable=False)
    rotation_period = Column(Integer)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    gravity = Column(String(250))
    population = Column(Integer)
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(Integer)
    liked_planet = Column(Integer, ForeignKey('liked_planets.id'))
    liked_planet_relationship = relationship("liked_planets", uselist=False)

class Liked_Planets(Base):
    __tablename__ = 'liked_planets'
    id = Column(Integer, primary_key=True)
    planet = Column(Integer, ForeignKey('planets.id'))
    planet_relationship = relationship(Planets)
    user = Column(Integer, ForeignKey('users.id'))
    user_relationship = relationship(Users)
    
class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True)
    mass = Column(Integer)
    height = Column(Integer)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
    planet = Column(Integer, ForeignKey('planets.id'))
    planet_relationship = relationship(Planets)
    starship = Column(Integer, ForeignKey('starships.id'))
    starship_relationship = relationship(Starships)
    liked_character = Column(Integer, ForeignKey('liked_characters.id'))
    liked_character_relationship = relationship("liked_Characters", uselist=False)
    

class Liked_Characters(Base):
    __tablename__ = 'liked_characters'
    id = Column(Integer, primary_key=True)
    character = Column(Integer, ForeignKey('characters.id'))
    character_relationship = relationship(Characters, uselist=False)
    user = Column(Integer, ForeignKey('users.id'))
    user_relationship = relationship(Users)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
