import uuid
from typing import Optional
from pydantic import BaseModel

TYPE_URI_S3 = 'type_uri_s3'
TYPE_URI_LOCAL_FS = 'type_uri_local_fs'

class URI(BaseModel):
    type: str
    location: str

class Item(BaseModel):
    id: Optional[str] = None
    collection_id: str
    name: Optional[str] = None
    uri: Optional[URI] = None

    def to_dict(self):
        if not hasattr(self, "id") or not getattr(self, "id"):
            self.id = uuid.uuid4().hex
        return super(Item, self).dict()

