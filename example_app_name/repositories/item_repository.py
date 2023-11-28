from db.alchemy_repository import SQLAlchemyRepository
from example_app_name.models.item_models import Item

class ItemRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__()

    async def create_item(self, name: str):
        async with self.get_session() as session:
            item = Item(name=name)
            await self.save(item, session)

    async def get_by_key(self, item_id: int):
        async with self.get_session() as session:
            return await self.find_by_key(Item, session, id=item_id)

    async def get_all_items(self):
        async with self.get_session() as session:
            return await self.find_all(Item, session)

        
# class ItemRepository(SQLAlchemyRepository):
#     def __init__(self):
#         async_engine, async_session = self.create_async_engine_session()
#         super().__init__(async_engine, async_session)

#     async def create_item(self, name: str):
#         async with self.get_session() as session:
#             item = Item(name=name)
#             await self.save(item, session)

#     async def get_by_key(self, item_id: int):
#         async with self.get_session() as session:
#             return await self.find_by_key(Item, session, id=item_id)

#     async def get_all_items(self):
#         async with self.get_session() as session:
#             return await self.find_all(Item, session)
