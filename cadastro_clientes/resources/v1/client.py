from fastapi import APIRouter

from cadastro_clientes.modules.client import insert
from cadastro_clientes.models.client import (
        InsertClientRequest, InsertClientResponse, CLIENT_DEFAULT_RESPONSE
        )


router = APIRouter()


@router.post("/insert", response_model=InsertClientResponse, status_code=200,
             summary="Gravar um JSON no banco de dados", responses=CLIENT_DEFAULT_RESPONSE)
async def save_client(client_data: InsertClientRequest):
    """
    Endpoint para efetuar a gravação de um cliente de forma assíncrona no banco de dados.
    """
    return {"result": [insert(client_data.dict())]}
