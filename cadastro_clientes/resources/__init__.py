from fastapi import APIRouter

from cadastro_clientes.resources.v1 import client, healthcheck


v1 = APIRouter()
v1.include_router(client.router, prefix="/client", tags=["client"])
v1.include_router(healthcheck.router, prefix="/health", tags=["healthcheck"])
