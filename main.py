import os
from fastapi import FastAPI
from azure.storage.blob import ContainerClient
from azure.storage.blob.aio import ContainerClient as ContainerClientAsync


if not os.getenv('AZURE_CONTAINER_URL'):
    raise Exception("Env variabl AZURE_CONTAINER_URL required")
container_url = os.getenv('AZURE_CONTAINER_URL')


app = FastAPI(docs_url="/")

@app.get("/ping")
def ping_pong():
    return "pong"


@app.get("/sync")
def sync():
    client = ContainerClient.from_container_url(container_url)
    blobs = []
    for blob in client.list_blobs():
        blobs.append(blob.name)
    return blobs
    
@app.get("/async")
async def a_sync():
    blobs = []
    async with ContainerClientAsync.from_container_url(container_url) as client:
        async for blob in client.list_blobs():
            blobs.append(blob.name)
    return blobs
    