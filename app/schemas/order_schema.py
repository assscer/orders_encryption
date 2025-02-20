from pydantic import BaseModel
from typing import List, Optional

class ProductSchema(BaseModel):
    name: str
    price: float
    quantity: int

class OrderCreate(BaseModel):
    customer_name: str
    total_price: float
    products: List[ProductSchema]

class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    status: Optional[str] = None
    total_price: Optional[float] = None

class OrderResponse(BaseModel):
    id: int
    customer_name: str
    status: str
    total_price: float

    class Config:
        orm_mode = True
