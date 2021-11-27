import uuid
from typing import Optional, List, Dict, Union
from datetime import datetime
from pydantic import BaseModel

from akyuu.model.item import Item

class Collection(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    owner: Optional[str] = "nobody"
    description: Optional[str] = None
    items: List[Item] = []

    def to_dict(self):
        if not hasattr(self, "id") or not getattr(self, "id"):
            self.id = uuid.uuid4().hex
        return super(Collection, self).dict()
