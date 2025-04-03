from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ProductSchema(BaseModel):
    name: str
    description: str
    category: str
    price: float
    images: List[str]
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    created_at: datetime = datetime.utcnow()

