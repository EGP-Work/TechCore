from pydantic import BaseModel

class StaffCreate(BaseModel):
    name: str
    email: str
    phone: int
    role: str

class StaffUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: int | None = None
    role: str | None = None