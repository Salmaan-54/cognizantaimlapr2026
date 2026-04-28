# creating all the tables
from ecommerce.configurations.mysql_conn import Base, engine
#  IMPORT MODELS FIRST (VERY IMPORTANT)
from ecommerce.models.customer import Customer
from ecommerce.models.catalog import Catalog 
from ecommerce.models.product import Product 

#create all the tables in the database
Base.metadata.create_all(bind = engine)

#make api call
from fastapi import FastAPI
from ecommerce.controller import customer_controller
from ecommerce.controller import catalog_controller
from ecommerce.controller import product_controller

app = FastAPI(
    title = "Just an API for Ecommerce",
    descripiton = "API for managing e-commerce operations.",
    version = "0.0.1"
)
app.include_router(customer_controller.router)
app.include_router(catalog_controller.router)
app.include_router(product_controller.router)