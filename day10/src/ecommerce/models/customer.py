# design orm for cutomer tablerfrom sqlalchemy 

from sqlalchemy import Column, DateTime, String, Integer

from ecommerce.configurations.mysql_conn import  Base
from ecommerce.models.full_name import FullName

class Customer(Base, FullName):
    __tablename__ = "customer"
    id = Column(Integer, primary_key = True, autoincrement = True)
    email = Column(String(150), unique = True, nullable = False)
    password = Column(String(10), nullable = False)
    created_at = Column(DateTime, nullable = False)
    updated_at = Column(DateTime, nullable = False)