from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.sales_order import SalesOrderCreate, SalesOrderResponse
from CRUD.sales_order import add_sales_order, get_sales_orders, get_sales_order_by_id, get_sales_order_by_customer_id
# delete_sales_order

router = APIRouter()

@router.post('/sales-orders')
def add_sales_order_route(
    sales_order: SalesOrderCreate, 
    db: Session = Depends(get_db)
):
    return add_sales_order(db, sales_order)

@router.get('/sales-orders')
def get_sales_orders_route(
    db: Session = Depends(get_db)
):
    return get_sales_orders(db)

@router.get("/sales-orders/{order_id}")
def get_sales_order_by_id_route(
    order_id: int, 
    db: Session = Depends(get_db)
):
    return get_sales_order_by_id(db, order_id)

@router.get("/customers/{customer_id}/sales-orders")
def get_sales_order_by_customer_id_route(
    customer_id: int,
    db: Session = Depends(get_db)
): 
    return get_sales_order_by_customer_id(db, customer_id)

# @router.delete("/sales-order/{order_id}")
# def delete_sales_order_route(
#     order_id: int,
#     db: Session = Depends(get_db)
# ):
#     return delete_sales_order(db, order_id)