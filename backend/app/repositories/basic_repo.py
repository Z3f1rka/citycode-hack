from abc import ABC, abstractmethod
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict): ...
    
    @abstractmethod
    async def find_all(self): ...

class Repository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict):
        instance = self.model(**data)
        self.session.add(instance)
        await self.session.flush()
        return instance

    async def find_all(self):
        res = await self.session.execute(select(self.model))
        return res.scalars().all()