from pydantic import BaseModel

class StockCreate(BaseModel):
    quantity: int
    product_id: int
    location_id: int

# class StockEdit(BaseModel):
#     quantity: int
#     product_id: int
#     location_id: int