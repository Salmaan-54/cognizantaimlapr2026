#create class individual using pydantic

from pydantic import BaseModel, Field, FieldValidator
from src.models.customer import Customer
from src.models.gender import Gender
from datetime import date

class Individual(BaseModel):
    individual_id: int = Field(..., gt=0, description="The unique identifier for the individual")
    customer: Customer
    gender: Gender
    dob: date = Field(..., description="The date of birth of the individual in YYYY-MM-DD format")

    @FieldValidator('dob')
    def validate_dob(cls, value):
        if value > date.today():
            raise ValueError("Date of birth cannot be in the future")
        age = (date.today() - value).days // 365
        if age < 18:
            raise ValueError("Individual must be at least 18 years old")
        return value