import logging
from typing import Tuple, Union

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from config.config import config
from sqlalchemy.future import select

logger = logging.getLogger(__name__)


class SQLAlchemyRepository:
    def __init__(self):
        self.async_engine = None
        self.session_local = None

    def create_async_engine_session(self) -> Tuple[AsyncEngine, sessionmaker]:
        if self.async_engine is None or self.session_local is None:
            self.async_engine = create_async_engine(**config()['db']['default'])
            self.session_local = sessionmaker(self.async_engine, class_=AsyncSession, expire_on_commit=False)
        return self.async_engine, self.session_local

    def initialize(self):
        self.create_async_engine_session()

    def get_session(self) -> AsyncSession:
        if self.async_engine is None or self.session_local is None:
            self.initialize()
        return self.session_local()

    async def save(self, model, session: AsyncSession) -> bool:
        try:
            async with session.begin():
                session.add(model)
            return True
        except SQLAlchemyError as e:
            logger.error(f"Failed to save data: {e}")
            raise e

    async def find_all(self, model_type, session: AsyncSession, **kwargs):
        stmt = select(model_type).filter_by(**kwargs)
        result = await session.execute(stmt)
        return result.scalars().all()

    async def find_by_key(self, model_type, session: AsyncSession, **kwargs: Union[int, str]):
        stmt = select(model_type).filter_by(**kwargs)
        result = await session.execute(stmt)
        return result.scalar()
    
     # async def delete(self, model, session: AsyncSession) -> bool:
    #     try:
    #         async with session.begin():
    #             session.delete(model)
    #         return True
    #     except SQLAlchemyError as e:
    #         logger.error(f"Failed to delete data: {e}")
    #         raise e
