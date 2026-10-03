from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.customer import CustomerCreate, CustomerUpdate
from CRUD.customer import add_customer, get_customers, get_customer_by_id, update_customer

router = APIRouter()

@router.post('/customers')
def add_customer_route(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    return add_customer(db, customer)

@router.get('/customers')
def get_customers_route(
    name: str | None = None,
    db: Session = Depends(get_db)
):
    return get_customers(db, name)

@router.get("/customers/{customer_id}")
def get_customer_by_id_route(
    customer_id : int,
    db: Session = Depends(get_db)
): 
    return get_customer_by_id(db, customer_id) 

@router.put("/customers/{customer_id}")
def update_customer_route(
    customer_id: int,
    data: CustomerUpdate,
    db: Session = Depends(get_db)
):
    return update_customer(db, customer_id, data)