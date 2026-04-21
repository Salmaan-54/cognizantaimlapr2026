#create customer class using pydantic

from pydantic import BaseModel, Field
from src.models.full_name import FullName

class Customer(BaseModel):
    customer_id: int = Field(..., gt=0, description="The unique identifier for the customer")
    name: FullName
    email: str = Field(..., pattern=r'^\S+@\S+\.\S+$', description="The email address of the customer")
    phone_number: str = Field(..., pattern=r'^\+\d{1,3}-\d{3}-\d{4}$', description="The phone number of the customer in E.164 format")