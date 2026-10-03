from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.location import LocationCreate, LocationUpdate
from database import get_db
from CRUD.location import add_location, get_locations, get_location, delete_location, update_location

router = APIRouter()

@router.post('/locations')
def add_location_route(
    location: LocationCreate,
    db: Session = Depends(get_db)
):
    return add_location(db, location)

@router.get('/locations')
def get_locations_route(
    db: Session = Depends(get_db)
):
    return get_locations(db)

@router.get('/locations/{location_id}')
def get_location_route(
    location_id: int,
    db: Session = Depends(get_db)
):
    return get_location(db, location_id)

@router.delete('/locations/{location_id}')
def delete_location_route(
    location_id: int,
    db: Session = Depends(get_db)
):
    return delete_location(db, location_id)

@router.put('/locations/{location_id}')
def update_location_route(
    location_id: int,
    data: LocationUpdate,
    db: Session = Depends(get_db)
):
    return update_location(db, location_id, data)