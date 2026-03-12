from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.routes.contract_route import router
from src.scheduler.start_scheduler import start_scheduler


@asynccontextmanager
async def lifespan(app: FastAPI):

    start_scheduler()
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(router)
