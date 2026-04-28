from pydantic import BaseModel, Field

class ProductRequest(BaseModel):
    product_name: str = Field(..., min_length = 5, max_length=150)
    price: float = Field(..., gt=0)
    stock_quantity: int = Field(..., gt=10)
    catalog_id: int = Field(..., gt=0)