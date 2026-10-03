from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime
from zoneinfo import ZoneInfo

WIB = ZoneInfo("Asia/Jakarta")

class SalesOrder(Base):
    __tablename__ = "sales_orders"
    order_id = Column(Integer, primary_key = True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    total = Column(Integer, nullable= False, default= 0)
    created_at = Column(DateTime(timezone= True), default= lambda: datetime.now(WIB))

    sales_order_items = relationship(
        "SalesOrderItem",
        back_populates= "sales_order"
    )
    customer = relationship(
        "Customer",
        back_populates= "sales_orders"
    )