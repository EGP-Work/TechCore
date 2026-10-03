from models.sales_order import SalesOrder
from schemas.sales_order import SalesOrderCreate, SalesOrderResponse
from sqlalchemy.orm import Session
from fastapi import HTTPException

def add_sales_order(db: Session, sales_order: SalesOrderCreate):
    new_sales_order = SalesOrder(customer_id = sales_order.customer_id)

    db.add(new_sales_order)
    db.commit()
    db.refresh(new_sales_order)
    return new_sales_order

def get_sales_orders(db: Session):
    sales_orders = db.query(SalesOrder).all()
    return sales_orders

def get_sales_order_by_customer_id(db:Session, customer_id: int):
    customer = db.query(SalesOrder).filter(SalesOrder.customer_id == customer_id).all()

    if not customer:
        raise HTTPException(status_code= 404, detail= "No Entry Found")

    return customer

def get_sales_order_by_id(db:Session, order_id: int):
    sales_order = db.query(SalesOrder).filter(SalesOrder.order_id == order_id).first()

    if sales_order is None:
        raise HTTPException(status_code= 404, detail= "No Entry Found")

    return sales_order

# def delete_sales_order(db: Session, order_id: int):
#     sales_order = db.query(SalesOrder).filter(SalesOrder.order_id == order_id).first()

#     if sales_order is None:
#         raise HTTPException(status_code= 404, detail= "No Entry Found")

#     db.delete(sales_order)
#     db.commit()
#     return sales_order
