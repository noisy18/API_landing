from typing import TypeVar, Generic, Type, Optional, Any, List, ClassVar
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, insert
from sqlalchemy.orm import DeclarativeMeta, Load
from sqlalchemy.engine import Result
from sqlalchemy.orm.interfaces import LoaderOption

ModelType = TypeVar("ModelType", bound=DeclarativeMeta)


class BaseRepository(Generic[ModelType]):
    model: Type[ModelType]
    options: Optional[List[LoaderOption]] = None

    def init(self, session: AsyncSession):
        if not hasattr(self, "model"):
            raise ValueError("Subclasses must define class-level 'model'")
        self.session = session

    def _with_related(self) -> List[Load]:
        return self.options or []

    async def create(self, returning: bool = False, **kwargs) -> ModelType:
        stmt = insert(self.model).values(**kwargs)
        if returning:
            stmt = stmt.returning(self.model)
        result: Result = await self.session.execute(statement=stmt)
        await self.session.commit()
        if returning:
            return result.scalar_one()

    async def exists(self, **filters) -> bool:
        stmt = select(self.model).filter_by(**filters)
        result = await self.session.execute(statement=stmt)
        return result.scalar_one_or_none() is not None

    async def filter_by(self, **filters) -> List[ModelType]:
        stmt = select(self.model).filter_by(**filters)
        result = await self.session.execute(statement=stmt)
        return result.scalars().all()