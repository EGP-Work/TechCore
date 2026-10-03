from pydantic import BaseModel

class CustomerCreate(BaseModel):
    name: str
    phone: int
    email: str

class CustomerUpdate(BaseModel):
    name: str | None = None
    phone: int | None = None
    email: str | None = None