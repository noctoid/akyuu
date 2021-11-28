import os
import time
import requests
import json

from typing import Optional
import typer

from akyuu.model.item import Item
from akyuu.model.collection import Collection

app = typer.Typer()


@app.command()
def collection(command: str, source_path: Optional[str] = "", collection_id: Optional[str] = ""):
    assert command in {"new", "get"}
    if command == "new":
        try:
            assert source_path != "" and source_path != None
        except AssertionError:
            raise typer.Exit(code=1)

        add_one_file(source_path)

    elif command == "get":
        try:
            assert collection_id != "" and collection_id != None
        except AssertionError:
            raise typer.Exit(code=1)

        collection = get_one_collection(collection_id)
        items = [get_one_item(item_id) for item_id in collection.items]

        print(collection)
        print(items)


    typer.Exit(0)

@app.command()
def item(command: str, source_path: Optional[str] = ""):
    assert command in {"new", "get"}
    if command == "new":
        try:
            assert source_path != "" and source_path != None
        except AssertionError:
            raise typer.Exit(code=1)

        uri = add_one_file(source_path)
        result = add_one_item("5d068bf83c8d48e5856ca8cd244b8646", uri)
        print(result)

    typer.Exit(0)


def current_epoch_time_in_ms():
    return int(time.time() * 1000)

def add_one_file(file_path: str):
    with open(file_path, 'rb') as f:
        file_content = f.read()
    url = "http://localhost:8000/bin_object/"

    payload = {}
    files = [
        ('data', (f"{current_epoch_time_in_ms()}-{os.path.basename(file_path)}", file_content, 'application/octet-stream'))
    ]
    response = requests.request("POST", url, headers={}, data=payload, files=files)
    return response.json()['data']['filename']

def add_one_item(collection_id: str, name: str):
    url = "http://localhost:8000/items/"
    payload = {
        "collection_id": collection_id,
        "name": name,
        "uri": {
            "type": "type_uri_s3",
            "location": name
        }
    }
    response = requests.request("POST", url, headers={'Content-Type': 'application/json'}, data=json.dumps(payload))
    return response


def get_one_collection(collection_id: str) -> Collection:
    url = f"http://localhost:8000/collections/{collection_id}"
    response = requests.request("GET", url, headers={'Content-Type': 'application/json'}, data=None)
    print(response.json()['data'])
    return Collection(**response.json()['data']['_source'])


def get_one_item(item_id: str):
    url = f"http://localhost:8000/items/{item_id}"
    response = requests.request("GET", url, headers={'Content-Type': 'application/json'}, data=None)
    return Item(**response.json()['data']['_source'])

if __name__ == "__main__":
    app()
