TechCore

TechCore V1 is a self made project using
-FastAPI
-Python
-Pydantic
-SQLite

Techcore is a project representing a real life inventory management system based on a tech store which sales hardware like mouse, keyboard, PC part, and etc. Tech core also have locations so for example there are TechCore in one city and there are also the TechCore warehouse so each stock location will be different.

The purpose of this project is to understand what it takes to build a inventory management system for a tech store as an example with the use of ai as minimal as possible, while also testing the capabilities and the depth of understanding what I've learned so far.
This project backend was mainly designed and built by me, meanwhile the frontend was developed by ChatGPT. I also did some brainstorming with the AI if my idea on building the project is correct or not or which is better.

TechCore V1 feature:
- Staff Management
- Category Management 
- Product Management
- Customer Management
- Location Management
- Stock Management
- Sales Order Management
- Sales Order Item Management

TechCore V1 Flow

Staff
    │
    ▼
TechCore

Category
    │
    ▼
 Product
    │
    ▼
 Stock ◄──── Location

Customer
    │
    ▼
Sales Order
    │
    ▼
Sales Order Item
    │
    ▼
Stock Update

TechCore V1 Explanation Flow
- Staff can control each product to be managed
- Each product have their own category
- Each product's stock have their own location since there are the store and the warehouse

- Customers can bought products
- When a customer makes a purchase it creates a sales order
- Each sales order have their own lists of items which will be calculated then the stock gets updated

Current Entity Relationship

Category ----< Product 

Product ----< Stock

Location ----< Stock

Customer ----< Sales Order

Sales Order ----< Sales Order Item

Sales Order Item ---- Product


V1 Limitations:
- Working supplier
- No buy orders so quantity of stock needs to be added manually
- Updating sales-order-items has some flaw which is the sales-order-items that can be changed is everything but product_id
- Sales-order-items doesnt have location log so if items sold we don't know which location sold the items
- Authentications / authorization
- Stock transfer from warehouse to store
- Working log book
- Status of the transaction (e.g, Pending, Completed, Cancelled)
These are intentionally not implemented yet. But on future version it will get better or maybe got implemented.

Future Infrastructure
- Docker
- PostgreSQL
