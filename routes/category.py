from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.category import CategoryCreate, CategoryUpdate
from CRUD.category import add_category, get_categories, get_category, update_category

router = APIRouter()

@router.post('/categories')
def add_category_route(
    category: CategoryCreate,
    db: Session = Depends(get_db)
):
    return add_category(db, category)

@router.get('/categories')
def get_categories_route(
    db: Session = Depends(get_db)
):
    return get_categories(db)

@router.get('/categories/{category_id}')
def get_category_route(
    category_id: int,
    db: Session = Depends(get_db)
):
    return get_category(db, category_id)

@router.put("/categories/{category_id}")
def update_category_route(
    category_id: int,
    data: CategoryUpdate,
    db: Session = Depends(get_db)
):
    return update_category(db, category_id, data)

