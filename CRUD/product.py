from models.product import Product
from models.stock import Stock
from schemas.product import ProductCreate, ProductUpdate
from sqlalchemy.orm import Session
from fastapi import HTTPException

def add_product(db: Session, product: ProductCreate):
    new_product = Product(
        name = product.name,
        sale_price = product.sale_price,
        category_id = product.category_id
        )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def get_product_by_id(db: Session, product_id:int):
    product = db.query(Product).filter(Product.product_id == product_id).first()

    if product is None:
        raise HTTPException(status_code= 404, detail= "Product Not Found")

    return product

def get_products(db: Session, name: str| None = None):
    query = db.query(Product)

    if name is not None:
        query = query.filter(Product.name == name)

    products = query.all()

    if not products:
        raise HTTPException(status_code= 404, detail= "Product Not Found with that name")

    return products

def delete_product(db:Session, product_id: int ):
    product = db.query(Product).filter(Product.product_id == product_id).first()

    if product is None:
        raise HTTPException(status_code= 404, detail= "Product Not Found")

    stock = db.query(Stock).filter(Stock.product_id == product_id & Stock.quantity > 0).first()

    if stock is None:
        raise HTTPException(status_code= 400, detail= "Cannot delete the product while there is still in stock")

    db.delete(product)
    db.commit()

    return{
        "Message": "Product has been deleted successfully"
    }

def update_product(db: Session, product_id:int, data:ProductUpdate ):
    product = db.query(Product).filter(Product.product_id == product_id).first()

    if product is None:
        raise HTTPException(status_code=404, detail= "Product Not Found")

    if data.name is not None:
        product.name = data.name

    if data.category_id is not None:
        product.category_id = data.category_id

    if data.sale_price is not None:
        product.sale_price = data.sale_price

    db.commit()
    db.refresh(product)
    return product


    