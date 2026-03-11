from fastapi import FastAPI

from src.api.routes.contract_route import router as contract_router

app = FastAPI()

app.include_router(contract_router)
