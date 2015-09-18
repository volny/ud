import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'
    # Example attributes:
    # String(250), Integer, relationship(Class), nullable=False, primary_key=True, ForeignKey('some_table.id')
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    zipcode = Column(String(5))

class MenuItem(Base):
    __tablename__ = 'menu_item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    # define the relationship for the FK above
    restaurant = relationship(Restaurant)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
