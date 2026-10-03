from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from schemas.sales_order_item import SalesOrderItemCreate, SalesOrderItemUpdate, SalesOrderItemResponse
from CRUD.sales_order_item import (add_sales_order_item, get_sales_order_items, get_sales_order_items_by_order_id,
                                   get_sales_order_items_by_product_id, update_sales_order_item)

router = APIRouter()

@router.post('/sales-order-items')
def add_sales_order_items_route(
    order_item: SalesOrderItemCreate,
    product_id: int,
    order_id: int,
    location_id: int,
    db: Session = Depends(get_db)
):
    return add_sales_order_item(db, order_item, product_id, order_id, location_id)

@router.get('/sales-order-items')
def get_sales_order_items_route(
    db: Session = Depends(get_db)
):
    return get_sales_order_items(db)

@router.get('/sales-orders/{order_id}/sales-order-items')
def get_sales_order_items_by_order_id_route(
    order_id: int,
    db: Session = Depends(get_db)
):
    return get_sales_order_items_by_order_id(db, order_id)

@router.get('/products/{product_id}/sales-order-items')
def get_sales_order_items_by_product_id_route(
    product_id: int,
    db: Session = Depends(get_db)
):
    return get_sales_order_items_by_product_id(db, product_id)

@router.put('/sales-order-items/{order_id}')
def update_sales_order_item_route(
    data: SalesOrderItemUpdate,
    order_id: int,
    product_id: int,
    location_id: int,
    db: Session = Depends(get_db)
):
    return update_sales_order_item(db, order_id, product_id, location_id, data)