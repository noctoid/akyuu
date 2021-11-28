import uuid
from typing import Optional, List, Dict, Union
from datetime import datetime
from pydantic import BaseModel

class Base(BaseModel):
    id: Optional[str] = None

    def to_dict(self):
        if not hasattr(self, "id") or not getattr(self, "id"):
            self.id = uuid.uuid4().hex
        return super(Base, self).dict()
