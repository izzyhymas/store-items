from fastapi import FastAPI

import json

from models import Item


app = FastAPI()

with open ("store_items.json", "r") as f:
    json_dict = json.load(f)


items: list[Item] = []

for item in json_dict:
    items.append(Item(**item))


@app.get("/items")
async def get_items() -> list[Item]: 
    return items

@app.post("/items")
async def add_item(item: Item) -> None:
    items.append(item)

@app.put("/items/{item_id}")
async def update_item(item_id: int, updated_item: Item) -> None:
    for i, item in enumerate(items):
        if item.id == item_id:
            items[i] = updated_item
            return

@app.delete("/items/{item_id}")
async def delete_item(item_id: int) -> None:
    for i, item in enumerate(items):
        if item.id == item_id:
            items.pop(i)
            return