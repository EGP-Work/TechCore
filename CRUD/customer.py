from models.customer import Customer
from schemas.customer import CustomerCreate, CustomerUpdate
from fastapi import HTTPException
from sqlalchemy.orm import Session

def add_customer(db: Session, customer: CustomerCreate):
    new_customer = Customer(
        name = customer.name,
        phone = customer.phone, 
        email = customer.email
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

def get_customers(db:Session, name: str| None = None):
    query = db.query(Customer)

    if name is not None:
        query =  query.filter(Customer.name == name)

    customers = query.all()

    if not customers:
        raise HTTPException(status_code= 404, detail= "No Customer Found with that name")

    return customers

def get_customer_by_id(db:Session, customer_id: int):
    customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()

    if customer is None:
        raise HTTPException(status_code= 404, detail= "No Customer Found")
    
    return customer

def update_customer(db:Session, customer_id: int, data: CustomerUpdate):
    customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()

    if customer is None:
        raise HTTPException(status_code= 404, detail= "No Customer Found")

    if data.name is not None:
        customer.name = data.name

    if data.phone is not None:
        customer.phone = data.phone

    if data.email is not None:
        customer.email = data.email

    db.commit()
    db.refresh(customer)
    return customer