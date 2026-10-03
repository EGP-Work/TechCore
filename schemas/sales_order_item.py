from pydantic import BaseModel

class SalesOrderItemCreate(BaseModel):
    quantity: int

class SalesOrderItemResponse(BaseModel):
    order_id: int
    product_id: int
    quantity: int
    per_unit_price: int
    subtotal: int

class SalesOrderItemUpdate(BaseModel):
    quantity: int | None = None
    per_unit_price: int | None = None