from models.sales_order_item import SalesOrderItem
from models.category import Category
from models.customer import Customer
from models.location import Location
from models.product import Product
from models.sales_order import SalesOrder
from models.staff import Staff
from models.stock import Stock

from routes.sales_order_item import router as sales_order_item_router
from routes.category import router as category_router
from routes.customer import router as customer_router
from routes.location import router as location_router
from routes.product import router as product_router
from routes.sales_order import router as sales_order_router
from routes.staff import router as staff_router
from routes.stock import router as stock_router

from fastapi import FastAPI
from database import Base, engine

app = FastAPI()

app.include_router(sales_order_item_router)
app.include_router(category_router) 
app.include_router(customer_router) 
app.include_router(location_router) 
app.include_router(product_router) 
app.include_router(sales_order_router)  
# app.include_router(staff_router) 
app.include_router(stock_router) 

Base.metadata.create_all(bind= engine)