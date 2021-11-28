import uuid
import pydantic
from typing import Optional
from akyuu.model.base import Base

TYPE_URI_S3 = 'type_uri_s3'
TYPE_URI_LOCAL_FS = 'type_uri_local_fs'

class URI(pydantic.BaseModel):
    type: str
    location: str

class Item(Base):
    collection_id: str
    name: Optional[str] = None
    uri: Optional[URI] = None

