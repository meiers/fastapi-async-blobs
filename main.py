from fastapi import FastAPI

app = FastAPI(docs_url="/")


@app.get("/ping")
def ping_pong():
    return "pong"
