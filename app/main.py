import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.routers.product import router

app = FastAPI()
app.include_router(router, prefix="/api")
@app.get("/")
async def index():
    return FileResponse("app/static/index.html")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1")