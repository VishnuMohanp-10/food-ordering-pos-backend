from pydantic import BaseModel
from typing import Dict , Optional

class ItemCreate(BaseModel):
    name:str
    brand:str
    category:str
    product_code: str
    branch_id: int

class ItemUpdate(BaseModel):
    name: Optional[str]
    brand: Optional[str]
    category: Optional[str]
    product_code:Optional[str]
    branch_id: Optional[int]


class VariantCreate(BaseModel):
    item_id : int
    variant_name: str
    selling_price: float
    cost_price: float
    quantity:int
    properties: Dict[str, str] ={}

class VariantUpdate(BaseModel):
    variant_name: Optional[str]
    selling_price: Optional[float]
    cost_price: Optional[float]
    quantity: Optional[int]
    properties: Optional[Dict[str, str]]

    

