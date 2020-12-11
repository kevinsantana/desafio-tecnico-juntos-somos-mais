from fastapi import APIRouter

from cadastro_clientes.resources.v1 import healthcheck, client

v1 = APIRouter()
v1.include_router(client.router, prefix="/database", tags=["database"])
v1.include_router(healthcheck.router, prefix="/health", tags=["healthcheck"])
