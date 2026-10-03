from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    sale_price: int
    category_id: int

class ProductUpdate(BaseModel):
    name: str | None = None
    sale_price: int | None = None
    category_id: int | None = None