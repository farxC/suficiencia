from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI

from controller.auth import auth_routes
from controller.wallet import wallet_routes
from db.setup_database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title="Carteira Digital",
    description="Carteira digital - Exame de Suficiência",
    version="1.0.0",
    lifespan=lifespan,
)

main_router = APIRouter(prefix="/api")

main_router.include_router(auth_routes)
main_router.include_router(wallet_routes)

app.include_router(main_router)
