from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from schemas.staff import StaffCreate, StaffUpdate
from CRUD.staff import add_staff, delete_staff, get_staff_by_id, get_staffs, update_staff

router = APIRouter()

@router.post("/staffs")
def add_staff_route(
    staff: StaffCreate,
    db: Session = Depends(get_db)
):
    return add_staff(db, staff)

@router.get("/staffs")
def get_staffs_route(
    role: str | None = None,
    db: Session = Depends(get_db)
):
    return get_staffs(db, role)

@router.get("/staffs/{staff_id}")
def get_staff_by_id_route(
    staff_id: int,
    db:Session = Depends(get_db)
):
    return get_staff_by_id(db, staff_id)

@router.delete("/staffs/{staff_id}")
def delete_staff_route(
    staff_id: int,
    db: Session = Depends(get_db)
):
    return delete_staff(db, staff_id)

@router.put("/staffs/{staff_id}")
def update_staff_route(
    staff_id: int,
    data: StaffUpdate,
    db: Session = Depends(get_db)
):
    return update_staff(db, staff_id, data)