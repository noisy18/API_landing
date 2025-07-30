from functools import cached_property
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.request import RequestRepository

class DB:
    def __init__(self, session: AsyncSession):
        self.session = session

    @cached_property
    def requests(self) -> RequestRepository:
        return RequestRepository(self.session)