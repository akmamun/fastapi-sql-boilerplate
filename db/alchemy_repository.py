import logging

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import DeclarativeMeta
from typing import Tuple, List, Optional, Union
from config.config import config
from sqlalchemy.future import select

logger = logging.getLogger(__name__)


class SQLAlchemyRepository:
    def __init__(self, async_engine, session_local):
        self.async_engine = async_engine
        self.session_local = session_local

    @classmethod
    def create_async_engine_session(cls) -> Tuple[AsyncEngine, AsyncSession]:
        async_engine = create_async_engine(**config()['db']['default'])
        async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
        return async_engine, async_session

    def get_session(self) -> AsyncSession:
        return self.session_local()

    async def save(self, model, session: AsyncSession) -> bool:
        try:
            async with session.begin():
                session.add(model)
            return True
        except SQLAlchemyError as e:
            logger.error(f"Failed to save data: {e}")
            raise e

    # async def delete(self, model, session: AsyncSession) -> bool:
    #     try:
    #         async with session.begin():
    #             session.delete(model)
    #         return True
    #     except SQLAlchemyError as e:
    #         logger.error(f"Failed to delete data: {e}")
    #         raise e

    async def find_all(self, model_type, session: AsyncSession, **kwargs):
        stmt = select(model_type).filter_by(**kwargs)
        result = await session.execute(stmt)
        return result.scalars().all()

    async def find_by_key(self, model_type, session: AsyncSession, **kwargs: Union[int, str]):
        stmt = select(model_type).filter_by(**kwargs)
        result = await session.execute(stmt)
        return result.scalar()