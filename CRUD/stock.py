from models.stock import Stock
from schemas.stock import StockCreate
from fastapi import HTTPException
from sqlalchemy.orm import Session

def add_stock(db:Session, stock: StockCreate):
    new_stock = Stock(
        quantity = stock.quantity,
        product_id = stock.product_id,
        location_id = stock.location_id
    )
    db.add(new_stock)
    db.commit()
    db.refresh(new_stock)
    return new_stock

def get_stock_by_quantity(db:Session, min_quantity: int | None = None, max_quantity:int | None = None):
    query = db.query(Stock)

    if min_quantity is not None:
        query = query.filter(Stock.quantity >= min_quantity)

    if max_quantity is not None: 
        query = query.filter(Stock.quantity <= max_quantity)

    stock = query.all()

    if not stock:
        raise HTTPException(status_code=404, detail= "No matching stock quantity")

    return stock

def get_stock_by_id(db:Session, stock_id: int):
    stock = db.query(Stock).filter(Stock.stock_id == stock_id).first()

    if stock is None:
        raise HTTPException(status_code=404, detail= "No matching stock data")

    return stock

def get_stock_by_location(db:Session, location_id: int):
    location = db.query(Stock).filter(Stock.location_id == location_id).all()
    
    if not location:
        raise HTTPException(status_code= 404, detail= "Location Not Found")

    return location

def get_stock_by_product(db:Session, product_id:int): 
    product = db.query(Stock).filter(Stock.product_id == product_id).first()
    
    if product is None:
        raise HTTPException(status_code= 404, detail= "Product Not Found")

    return product
