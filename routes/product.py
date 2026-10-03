from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.product import ProductCreate, ProductUpdate
from CRUD.product import add_product, get_products, get_product_by_id, delete_product, update_product

router = APIRouter()

@router.post('/products')
def add_product_route(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    return add_product(db, product)

@router.get("/products")
def get_products_route(
    name: str | None = None,
    db: Session = Depends(get_db)
):
    return get_products(db, name)

@router.get("/products/{product_id}")
def get_product_by_id_route(
    product_id: int,
    db: Session = Depends(get_db)
):
    return get_product_by_id(db, product_id)

@router.delete("/products/{product_id}")
def delete_product_route(
    product_id: int,
    db: Session = Depends(get_db)
):
    return delete_product(db, product_id)

@router.put("/products/{product_id}")
def update_product_route(
    product_id: int,
    data: ProductUpdate,
    db: Session = Depends(get_db)
):
    return update_product(db, product_id, data)

