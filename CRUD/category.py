from models.category import Category
from schemas.category import CategoryCreate, CategoryUpdate
from sqlalchemy.orm import Session
from fastapi import HTTPException

def add_category(db: Session, category: CategoryCreate):
    new_category = Category(name = category.name)

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category

def get_categories(db: Session):
    categories = db.query(Category).all()

    return categories

def get_category(db:Session, category_id: int):
    category = db.query(Category).filter(Category.category_id == category_id).first()

    if category is None:
        raise HTTPException(status_code= 404, detail= "Entry Not Found")

    return category

def update_category(db:Session, category_id: int, data: CategoryUpdate ):
    staff = db.query(Category).filter(Category.category_id == category_id).first()

    if staff is None:
        raise HTTPException(status_code= 404, detail= "Entry Not Found")
    if data.name is not None:
        staff.name = data.name 

    db.commit()
    db.refresh(staff)
    return staff
