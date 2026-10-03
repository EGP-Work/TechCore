from models.location import Location
from models.stock import Stock
from schemas.location import LocationCreate, LocationUpdate
from fastapi import HTTPException
from sqlalchemy.orm import Session

def add_location(db: Session, location: LocationCreate):
    new_location = Location(
        name = location.name,
        address = location.address
    )

    db.add(new_location)
    db.commit()
    db.refresh(new_location)
    return new_location

def get_locations(db: Session):
    locations = db.query(Location).all()
    return locations

def get_location(db: Session, location_id: int):
    location = db.query(Location).filter(Location.location_id == location_id).first()

    if location is None:
        raise HTTPException(status_code= 404, detail= "Location Not Found")

    return location

def update_location(db: Session, location_id: int, data: LocationUpdate):
    location = db.query(Location).filter(Location.location_id == location_id).first()

    if location is None:
        raise HTTPException(status_code= 404, detail= "Location Not Found")

    if data.name is not None:
        location.name = data.name

    if data.address is not None:
        location.address = data.address

    db.commit()
    db.refresh(location)
    return location

def delete_location(db: Session, location_id: int):
    location = db.query(Location).filter(Location.location_id == location_id).first()

    if location is None:
        raise HTTPException(status_code= 404, detail= "Location Not Found")

    stock_check = db.query(Stock).filter(Stock.location_id == location_id & Stock.quantity > 0).first()

    if stock_check is None:
        raise HTTPException(status_code= 400, detail= "Cannot delete location while there is stock")

    db.delete(delete_location)
    db.commit()
    return{
        "Message": "Location has been deleted successfully"
    }
    
