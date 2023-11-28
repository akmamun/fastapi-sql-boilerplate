import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app_name.models.item_models import Base
from config.config import config

async def migrate():
    async_engine =  create_async_engine(**config()['db']['default'])
    async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(migrate())
