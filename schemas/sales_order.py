from pydantic import BaseModel, field_serializer
from datetime import datetime

class SalesOrderCreate(BaseModel):
    customer_id: int 

class SalesOrderResponse(BaseModel):
    sales_order_id: int
    customer_id: int
    created_at: datetime
    total: int
