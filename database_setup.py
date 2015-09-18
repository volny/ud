"""
This app implements the basic functionality of a FOOD DELIVERY NETWORK like mjam.net.
There are restaurants, each has a menu. People can put items in their 'cart', prices are added up. Upon checkout there is just a splashscreen saying "You've ordered X,Y and Z for A$".
"""

import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# an instance of SQLAs declarative_base.
# let's SQLA know that the classes used here are 'special' SQLA classes...they correspond to tables!
Base = declarative_base()

class Restaurant(Base):
    # Table representation `__tablename__` is reserved to let SQLA know which table this class is refering to
    __tablename__ = 'restaurant'
    # Mapping. 
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

# at EOF
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
