import io
from fastapi import UploadFile
from akyuu.model.response import HttpReponseBody

import akyuu.drivers.minio_driver

class ObjectHandler:

    async def add_bin_object(self, data: UploadFile):
        result = await akyuu.drivers.minio_driver.put_object(data.filename, data)
        return HttpReponseBody(status="success", data={"filename": data.filename})

    async def get_object(self, name):
        return HttpReponseBody(status="success", data=await akyuu.drivers.minio_driver.get_object(name))

