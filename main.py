import os

from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()
load_dotenv()

DATABASE_URL = f"""postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}
@db:5432/{os.getenv('POSTGRES_DB')}"""


@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI in Docker!"}
