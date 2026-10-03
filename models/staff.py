from sqlalchemy import String, Integer, Column
from database import Base

class Staff(Base):
    __tablename__ = "staffs"
    staff_id = Column(Integer, primary_key= True)
    name = Column(String)
    email = Column(String)
    phone = Column(Integer)
    role = Column(String)


