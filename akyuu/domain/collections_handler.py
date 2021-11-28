import uuid
from typing import Tuple, Dict, List
from elasticsearch import exceptions

import akyuu.drivers.elastic
from akyuu.model.item import Item
from akyuu.model.response import HttpReponseBody
from akyuu.model.collection import Collection

es_adapter = akyuu.drivers.elastic.ElasticDriver()


class CollectionsHandler:
    INDEX_NAME = "collections_"

    async def create(self, collection: Collection) -> HttpReponseBody:
        collection_id = await es_adapter.create(
            index=self.INDEX_NAME, document=collection.to_dict())
        return HttpReponseBody(status="success", data={"collection_id": collection_id})

    async def get(self, collection_id) -> HttpReponseBody:
        try:
            return HttpReponseBody(status="success", data=await es_adapter.get(index=self.INDEX_NAME, id=collection_id))
        except exceptions.NotFoundError:
            return HttpReponseBody(status="not_found")

    async def delete(self, collection_id) -> HttpReponseBody:
        try:
            return HttpReponseBody(status="success", data=await es_adapter.delete(index=self.INDEX_NAME, id=collection_id))
        except exceptions.NotFoundError:
            return HttpReponseBody(status="not_found")

    async def append_item(self, collection_id: str, item: Item):
        await es_adapter.append_to_array_in_doc(
            index=self.INDEX_NAME, id=collection_id, array_field_name="items", to_append=item.id)
