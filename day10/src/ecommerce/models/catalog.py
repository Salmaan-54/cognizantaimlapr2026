# design orm for cutomer tablerfrom sqlalchemy 

from sqlalchemy import Column, String, Integer

from ecommerce.configurations.mysql_conn import  Base

class Catalog(Base):
    __tablename__ = "catalog"
    catalog_id = Column(Integer, primary_key = True, autoincrement = True)
    catalog_name = Column(String(100), nullable = False)
    description = Column(String(255), nullable = True)