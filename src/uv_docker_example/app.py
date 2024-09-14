"""
A simple FASTAPI app server to demonstrate it running with Astral.sh uv Python package management
""""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
  return "This is the FASTAPI server running on Docker"
