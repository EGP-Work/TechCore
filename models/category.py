from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from database import Base

class Category(Base):
    __tablename__ = "categories"
    category_id = Column(Integer, primary_key= True)
    name = Column(String)

    products = relationship(
        "Product", 
        back_populates= "category"
    )