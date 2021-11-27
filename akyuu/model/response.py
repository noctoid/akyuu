from typing import Optional, Dict
from pydantic import BaseModel


class HttpReponseBody(BaseModel):
    status: str
    data: Optional[Dict] = None
