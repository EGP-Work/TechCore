from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from database import Base

class Location(Base): 
    __tablename__ = "locations"
    location_id = Column(Integer, primary_key= True)
    name = Column(String)
    address = Column(String)

    stocks = relationship(
        "Stock", 
        back_populates= "location"
    )