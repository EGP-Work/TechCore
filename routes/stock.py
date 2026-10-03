from fastapi import Depends, APIRouter
from database import get_db
from schemas.stock import StockCreate
from sqlalchemy.orm import Session
from CRUD.stock import add_stock, get_stock_by_id, get_stock_by_location, get_stock_by_product, get_stock_by_quantity

router = APIRouter()

@router.post('/stocks')
def add_stock_route(
    stock: StockCreate,
    db: Session = Depends(get_db)    
):
    return add_stock(db, stock)

@router.get('/stocks/{stock_id}')
def get_stock_by_id_route(
    stock_id : int,
    db:Session = Depends(get_db)
):
    return get_stock_by_id(db, stock_id)

@router.get('/locations/{location_id}/stocks')
def get_stock_by_location_route(
    location_id: str,
    db: Session = Depends(get_db)
):
    return get_stock_by_location(db, location_id)

@router.get('/products/{product_id}/stocks')
def get_stock_by_product_route(
    product_id: str,
    db: Session = Depends(get_db)
):
    return get_stock_by_product(db, product_id)

@router.get('/stocks')
def get_stock_by_quantity_route(
    min_quantity: int | None = None,
    max_quantity: int |None = None,
    db: Session = Depends(get_db)
):
    return get_stock_by_quantity(db, min_quantity, max_quantity)

