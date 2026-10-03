from pydantic import BaseModel

class LocationCreate(BaseModel):
    name: str
    address: str

class LocationUpdate(BaseModel):
    name: str | None = None
    address: str | None = None