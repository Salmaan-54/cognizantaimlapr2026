# create customer response dto
# This file defines the Customer REsponse DTO (Data Transfer Object) for handling customer responses.

from ecommerce.dtos.full_name_request import FullNameRequest
from pydantic import BaseModel, EmailStr, Field

class CustomerResponse(BaseModel):
    id: int
    full_name: FullNameRequest
    email: EmailStr
    password: str
    created_at: str
    updated_at: str