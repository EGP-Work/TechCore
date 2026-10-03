from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key= True)
    name = Column(String)
    sale_price = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.category_id'))

    category = relationship(
        "Category", 
        back_populates= "products"
    )
    stocks = relationship(
        "Stock",
        back_populates= "product"
    )
    sales_order_items = relationship(
        "SalesOrderItem",
        back_populates= "products"
    )