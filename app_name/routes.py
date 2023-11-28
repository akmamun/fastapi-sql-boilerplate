from app_name.controllers.item_controller import ItemController
from fastapi.routing import APIRoute

item_controller = ItemController()


async def health_check():
    return {"status": "OK"}


routers = [
    APIRoute('/', health_check, methods=["GET"]),
    APIRoute('/items/', item_controller.get_all_items, methods=["GET"]),
    # APIRoute('/items/paginate/',
    #          todo_controller.get_all_item_with_pagination, methods=["GET"]),
    APIRoute('/items/', item_controller.create_item, methods=["POST"]),
    APIRoute('/items/{item_id}', item_controller.get_item, methods=["GET"]),

]
