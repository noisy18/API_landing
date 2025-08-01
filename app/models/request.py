from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy import DateTime
from app.settings import get_current_time

from app.db.base import Base

class Request(Base):
    __tablename__ = "Requests"

    name: Mapped[str] = mapped_column(String, nullable=False)
    surname: Mapped[str] = mapped_column(String, nullable=False, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(20), unique=False, index=False, nullable=False)
    created_at: Mapped[str] = mapped_column(String, nullable=False, default=lambda: get_current_time())