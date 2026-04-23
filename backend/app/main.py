from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.db.database import init_db
from app.routers import tickets


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print("schema ready")
    yield


app = FastAPI(title="DevSupport Copilot", version="0.2.0", lifespan=lifespan)
app.include_router(tickets.router)


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=False)
