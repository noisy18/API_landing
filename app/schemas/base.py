from pydantic import BaseModel
from datetime import datetime

class BaseSchema(BaseModel):
    id: int
    created_at: datetime