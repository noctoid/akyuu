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
        es_doc = item.to_dict()
        item_id = await es_adapter.create(
            index=self.INDEX_NAME, id=item.id, document=es_doc)
        await CollectionsHandler().append_item(item.collection_id, item)
        return HttpReponseBody(status="success", data={"item_id": item_id})
