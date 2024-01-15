from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def pong():
    return {"message": "Hello World from FastAPI in Docker!"}
