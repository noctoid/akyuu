import io
from minio import Minio

client = Minio("127.0.0.1:9000/", "mmz78ZEa9kCr9LQHD6UCg0XIbI7Vy5M", "gmgYdncVMiTD9NKt7TrNgiv3dNWaPtM", secure=False)

async def put_object(name: str, data):
    content = await data.read()
    print(len(content))
    return client.put_object("akyuu_data", name, io.BytesIO(content), length=len(content))

async def get_object(name: str):
    return client.get_object("akyuu_data", name)
