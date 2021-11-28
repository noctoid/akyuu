import uuid
from typing import List, Any
from elasticsearch import Elasticsearch, exceptions

from akyuu.model.base import Base

GEN_UUID = uuid.uuid4
es_adapter = Elasticsearch()

class ElasticDriver:
    async def execute_command(self, func, **keywords):
        try:
            return func(**keywords)
        except exceptions.NotFoundError:
            raise exceptions.NotFoundError

    async def create(self, index,*, document: dict):
        print(document)
        await self.execute_command(es_adapter.index, index=index, id=document['id'], document=document)
        return document['id']

    async def get(self, index, id):
        return await self.execute_command(es_adapter.get, index=index, id=id)

    async def delete(self, index, id):
        return await self.execute_command(es_adapter.delete, index=index, id=id)

    async def patch(self, *, index, id, update_dict):
        es_adapter.update(index=index, id=id, body=update_dict)

    async def append_to_array_in_doc(self, *, index, id, array_field_name: str, to_append: Any):
        es_adapter.update(index=index, id=id, body={
            "script": {
                "source": f"ctx._source.{array_field_name}.add(params.to_append)",
                "lang": "painless",
                "params": {
                    "to_append": to_append
                }
            }
        })
