from sqlalchemy import Integer, Column, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from database import Base

class Stock(Base):
    __tablename__ = "stocks"
    stock_id = Column(Integer, primary_key= True)
    quantity = Column(Integer)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    location_id = Column(Integer, ForeignKey('locations.location_id'))

    product = relationship(
        "Product", 
        back_populates= "stocks"
    )
    location = relationship(
        "Location",
        back_populates= "stocks"
    )

    __table_args__ = (UniqueConstraint('product_id', 'location_id'),)