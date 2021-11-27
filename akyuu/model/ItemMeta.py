from typing import Optional
from pydantic import BaseModel

class ItemMeta(BaseModel):
    id: str
    description: Optional[str] = None
