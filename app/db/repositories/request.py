from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.request import Request
from app.schemas.request import RequestCreateSchema
from app.db.repositories.base_repository import BaseRepository


class RequestRepository(BaseRepository[Request]):
    model = Request

    def __init__(self, session: AsyncSession):
        super().init(session)
    
    async def create_request(self, request: RequestCreateSchema) -> Request:
        # return await self.create(
        #     name=request.name,
        #     surname=request.surname,
        #     email=request.email,
        #     phone=request.phone,
        #     returning=True
        # )
        instance = self.model(
            name=request.name,
            surname=request.surname,
            email=request.email,
            phone=request.phone,
            created_at=request.created_at
        )
        self.session.add(instance)
        await self.session.flush()
        await self.session.refresh(instance)
        return instance
    
    async def get_request_by_email(self, email: str) -> Optional[Request]:
        requests = await self.filter_by(email=email)
        return requests[0] if requests else None