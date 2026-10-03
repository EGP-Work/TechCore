from models.staff import Staff
from schemas.staff import StaffCreate, StaffUpdate
from sqlalchemy.orm import Session
from fastapi import HTTPException

def add_staff(db: Session, staff: StaffCreate):
    new_staff = Staff(
        name = staff.name,
        email = staff.email,
        role = staff.role,
        phone = staff.phone
        )

    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)
    return new_staff

def get_staffs(db:Session, role: str | None = None):
    query = db.query(Staff)

    if role is not None:
        query = query.filter(Staff.role == role)

    staff = query.all()

    if not staff:
        raise HTTPException(status_code= 404, detail= "Entry not found")
        
    return staff

def get_staff_by_id(db:Session, staff_id: int):
    staff = db.query(Staff).filter(Staff.staff_id == staff_id).first()

    if staff is None:
        raise HTTPException(status_code= 404, detail= "Entry not found")
        
    return staff

def update_staff(db:Session, staff_id:int, data:StaffUpdate):
    staff = db.query(Staff).filter(Staff.staff_id == staff_id).first()

    if staff is None:
        raise HTTPException(status_code= 404, detail= "Entry not found")

    if data.name is not None:
        staff.name = data.name

    if data.email is not None:
        staff.email = data.email

    if data.phone is not None:
        staff.phone = data.phone

    if data.role is not None:
        staff.role = data.role

    db.commit()
    db.refresh(staff)
    return staff

def delete_staff(db:Session, staff_id: int):
    staff = db.query(Staff).filter(Staff.staff_id == staff_id).first()

    if staff is None:
        raise HTTPException(status_code= 404, detail= "Entry not found")

    db.delete(staff)
    db.commit()   
    return staff

