from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class SalesOrderItem(Base):
    __tablename__ = "sales_order_items"
    order_id = Column(Integer, ForeignKey("sales_orders.order_id"), primary_key= True)
    product_id = Column(Integer, ForeignKey("products.product_id"), primary_key= True)
    quantity = Column(Integer)
    per_unit_price = Column(Integer)
    subtotal = Column(Integer, default= 0)

    sales_order = relationship(
        "SalesOrder",
        back_populates= "sales_order_items"
    )
    products = relationship(
        "Product", 
        back_populates= "sales_order_items"
    )