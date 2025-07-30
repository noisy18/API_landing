from pydantic import EmailStr, BaseModel, Field
from app.schemas.base import BaseSchema
import re
from datetime import datetime

class RequestCreateSchema(BaseModel):
    name: str
    surname: str
    email: EmailStr
    phone: str = Field(example="+79991234567")
    created_at: datetime

    @classmethod
    def validate_phone(cls, phone: str) -> str:
        pattern = r'^\+?\d{10,15}$'
        if not re.fullmatch(pattern, phone):
            raise ValueError("Неверный формат телефона. Пример: +79991234567")
        return phone

    def model_post_init(self, __context):
        self.phone = self.validate_phone(self.phone)

class RequestResponseSchema(BaseSchema):
    name: str
    surname: str
    email: EmailStr
    phone: str = Field(example="+79991234567")
    created_at: datetime

    class Config:
        from_attributes = True
