from akyuu.model.base import Base

class Resource(Base):
    item_id: str
    name: str
    data: bytearray
