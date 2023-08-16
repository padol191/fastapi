import time
from pathlib import Path

from fastapi import FastAPI, APIRouter, Request
from fastapi.middleware.cors import CORSMiddleware


from app.api.api_v1.api import api_router
from app.core.config import settings
from .db.session import engine
from .db.base_class import Base
from .models import models

BASE_PATH = Path(__file__).resolve().parent

models.Base.metadata.create_all(engine)
extend_existing=True
root_router = APIRouter()
app = FastAPI(title="Apollo Lite APIs", openapi_url=f"/openapi.json")

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_origin_regex=settings.BACKEND_CORS_ORIGIN_REGEX,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@root_router.get("/", status_code=200)
def root():
    return "Welcome to Apollo Lite"
    


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.include_router(api_router)
app.include_router(root_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
