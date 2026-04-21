#create address class associate to customer using pydantic

from pydantic import BaseModel, Field
from src.models.customer import Customer

class Address(BaseModel):
    cusotmer: Customer
    street: str = Field(..., pattern="^.*$", description="The street address of the customer")
    city: str = Field(..., pattern="^.*$", description="The city of the customer")
    state: str = Field(..., pattern="^.*$", description="The state of the customer")
    zip_code: str = Field(..., pattern="^.*$", description="The zip code of the customer in 5 or 9 digit format")
    country: str = Field(..., pattern="^.*$", description="The country of the customer")