from fastapi import FastAPI

app = FastAPI()


def hello():
    print("Hello world from the docker container")


@app.get("/")
async def root():
    return "This is a FASTAPI sending this message from docker "
