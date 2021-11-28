import uuid
from elasticsearch import Elasticsearch

from akyuu.model.item import Item
from akyuu.model.response import HttpReponseBody
from akyuu.drivers.elastic import ElasticDriver

from akyuu.domain.collections_handler import CollectionsHandler

GEN_UUID = uuid.uuid4
es_adapter = ElasticDriver()

class ItemsHandler:
    INDEX_NAME = "items_"

    async def create(self, item: Item) -> HttpReponseBody:
        item_id = await es_adapter.create(
            index=self.INDEX_NAME, document=item.to_dict())
        await CollectionsHandler().append_item(item.collection_id, item)
        return HttpReponseBody(status="success", data={"item_id": item_id})

    async def get(self, item_id: str) -> Item:
        return await es_adapter.get(self.INDEX_NAME, item_id)

