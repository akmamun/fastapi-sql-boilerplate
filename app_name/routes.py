from app_name.controllers.item_controller import ItemController
from fastapi.routing import APIRoute

item_controller = ItemController()


async def health_check():
    return {"status": "OK"}

routers = [
    APIRoute('/health/', health_check, methods=["GET"]),
    APIRoute('/v1/items/', item_controller.get_all_items, methods=["GET"]),
    # APIRoute('/v1/items/paginate/',
    #          todo_controller.get_all_item_with_pagination, methods=["GET"]),
    APIRoute('/v1/items/', item_controller.create_item, methods=["POST"]),
    APIRoute('/v1/items/{item_id}', item_controller.get_item, methods=["GET"]),
]