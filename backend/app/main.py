import uvicorn
from fastapi import FastAPI

from app.routers import tickets

app = FastAPI(title="DevSupport Copilot", version="0.1.0")
app.include_router(tickets.router)


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=False)
