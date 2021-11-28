import uuid
from typing import Optional, List, Dict, Union
from datetime import datetime

from akyuu.model.item import Item
from akyuu.model.base import Base

class Collection(Base):
    name: Optional[str] = None
    owner: Optional[str] = "nobody"
    description: Optional[str] = None
    items: List[str] = []
