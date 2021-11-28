from typing import Optional
from fastapi import FastAPI, File, UploadFile

from akyuu.domain.collections_handler import CollectionsHandler
from akyuu.domain.items_handler import ItemsHandler
from akyuu.domain.object_handler import ObjectHandler
from akyuu.model.item import Item
from akyuu.model.collection import Collection
from akyuu.model.response import HttpReponseBody

app = FastAPI()

STATUS_MAP = {
    "success": 200,
    "not_found": 404,
    "forbidden": 403,
    "internal_server_error": 500,
}

def make_response(result: HttpReponseBody):
    return {"status": STATUS_MAP[result.status], "data": result.data}

@app.get("/ping")
async def ping():
    return {"msg": "pong"}


@app.post("/collections/")
async def post_collection(collection: Collection):
    return make_response(await CollectionsHandler().create(collection=collection))


@app.get("/collections/{collection_id}")
async def get_collection(collection_id: str):
    return make_response(await CollectionsHandler().get(collection_id))


@app.delete("/collections/{collection_id}")
async def delete_collection(collection_id: str):
    return make_response(await CollectionsHandler().delete(collection_id))


@app.post("/items/")
async def post_item(item: Item):
    return make_response(await ItemsHandler().create(item))

@app.get("/items/{item_id}")
async def get_item(item_id: str):
    return make_response(HttpReponseBody(status='success', data={**await ItemsHandler().get(item_id)}))


@app.post("/bin_object/")
async def post_bin_object(data: UploadFile = File(...)):
    return make_response(await ObjectHandler().add_bin_object(data))

@app.get("/bin_object/{object_name}")
async def get_bin_object(object_name):
    return make_response(await ObjectHandler().get_object(object_name))
