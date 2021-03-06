from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/")
async def public(request: Request):
    print(await request.body())


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
