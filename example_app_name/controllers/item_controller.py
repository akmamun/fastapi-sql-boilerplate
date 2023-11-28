from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

from example_app_name.repositories.item_repository import ItemRepository

class ItemController:
    def __init__(self):
        self.item_repository = ItemRepository()

    async def create_item(self, request_data: dict):
        item_name = request_data.get('name')

        if not item_name:
            raise HTTPException(status_code=400, detail="Item name is required")

        await self.item_repository.create_item(item_name)

        return {"message": "Item created successfully"}

    async def get_item(self, item_id: int):
        item = await self.item_repository.get_by_key(item_id=item_id)

        if not item:
            raise HTTPException(status_code=404, detail="Item not found")

        return {"id": item.id, "name": item.name}

    async def get_all_items(self):
        items = await self.item_repository.get_all_items()
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"data": [item.as_dict() for item in items],
                     "code": status.HTTP_200_OK,
                     "message": "Data Found"}
        )



# #     async def get_all_item_with_pagination(
# #         self,
# #         limit: int = Query(10, description="Number of items per page", gt=0),
# #         offset: int = Query(0, description="Number of items to skip", ge=0),
# #         session: AsyncSession = Depends(get_async_session),
# #     ):
# #             # Build the base query
# #         query = select(Item)

# #         # Use the paginate function
# #         items = await paginate(
# #             session=session,
# #             query=query,
# #             limit=limit,
# #             offset=offset,
# #             sort_by="id",
# #             sort_desc=True,
# #         )

# #         return JSONResponse(
# #             status_code=200,
# #             content={"data": [item.as_dict() for item in items],
# #                         "code": 200,
# #                         "message": "Data Found"})
