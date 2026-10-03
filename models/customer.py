from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship
from database import Base

class Customer(Base):
    __tablename__ = "customers"
    customer_id = Column(Integer, primary_key= True)
    name = Column(String)
    phone = Column(Integer)
    email = Column(String)

    # Change phone to STR cus the number 0 in front is not possible

    sales_orders = relationship(
        "SalesOrder",
        back_populates= "customer"
    )