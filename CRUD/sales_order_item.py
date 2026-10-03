from models.sales_order_item import SalesOrderItem
from models.product import Product
from models.sales_order import SalesOrder
from models.stock import Stock
from schemas.sales_order_item import SalesOrderItemCreate, SalesOrderItemUpdate
from sqlalchemy.orm import Session
from fastapi import HTTPException

def add_sales_order_item(db:Session, sales_order_item: SalesOrderItemCreate, product_id: int, order_id: int, location_id: int):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    order = db.query(SalesOrder).filter(SalesOrder.order_id == order_id).first()
    stock = db.query(Stock).filter(Stock.product_id == product_id, location_id == location_id).first()

    if product is None:
        raise HTTPException(status_code= 404, detail= "Product doesn't exist")
    if stock is None:
        raise HTTPException(status_code= 404, detail= "Stock doesn't exist")
    if order is None:
        raise HTTPException(status_code= 404, detail= "Sales order doesn't exist")

    new_sales_order_item = SalesOrderItem(
        order_id = order_id,
        product_id = product.product_id,
        quantity = sales_order_item.quantity,
        per_unit_price = product.sale_price,
        subtotal = sales_order_item.quantity * product.sale_price
    )

    if new_sales_order_item.quantity > stock.quantity:
        raise HTTPException(status_code= 400, detail= "Data can't be added because of not enough stock available")

    stock.quantity -= new_sales_order_item.quantity 
    order.total += new_sales_order_item.subtotal
    
    db.add(new_sales_order_item)
    db.commit()
    db.refresh(new_sales_order_item)
    return new_sales_order_item

def get_sales_order_items(db:Session):
    sales_order_item = db.query(SalesOrderItem).all()
    return sales_order_item

def get_sales_order_items_by_order_id(db:Session, order_id: int):
    sales_order_item = db.query(SalesOrderItem).filter(SalesOrderItem.order_id == order_id).all()

    if not sales_order_item:
        raise HTTPException(status_code= 404, detail= "Sales order item not found")

    return sales_order_item

def get_sales_order_items_by_product_id(db:Session, product_id: int):
    sales_order_item = db.query(SalesOrderItem).filter(SalesOrderItem.product_id == product_id).all()
    
    if not sales_order_item:
        raise HTTPException(status_code= 404, detail= "Sales order item not found")

    return sales_order_item

def update_sales_order_item(db:Session, order_id: int, product_id: int, location_id:int, data: SalesOrderItemUpdate):
    sales_order_item = db.query(SalesOrderItem).filter(SalesOrderItem.order_id == order_id, SalesOrderItem.product_id == product_id).first()
    product = db.query(Product).filter(Product.product_id == product_id).first()
    stock = db.query(Stock).filter(Stock.product_id == product_id, Stock.location_id == location_id).first()
    order = db.query(SalesOrder).filter(SalesOrder.order_id == order_id).first()

    if sales_order_item is None:
        raise HTTPException(status_code= 404, detail= "Sales order item not found")
    if product is None:
        raise HTTPException(status_code= 404, detail= "product not found")
    if stock is None:
        raise HTTPException(status_code= 404, detail= "Stock not found")

    old_product_quantity = stock.quantity + sales_order_item.quantity

    if data.quantity is not None and old_product_quantity < data.quantity:
        raise HTTPException(status_code= 400, detail= "Cannot be updated because of not enough available stock")

    order.total -= sales_order_item.subtotal

    if data.per_unit_price is not None:
        sales_order_item.per_unit_price = data.per_unit_price
    if data.quantity is not None:
        sales_order_item.quantity = data.quantity
        stock.quantity = old_product_quantity - sales_order_item.quantity

    sales_order_item.subtotal = sales_order_item.per_unit_price * sales_order_item.quantity
    order.total += sales_order_item.subtotal

    db.commit()
    db.refresh(sales_order_item)
    return sales_order_item 