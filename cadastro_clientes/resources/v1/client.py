from fastapi import APIRouter, Body, Request, Query

from cadastro_clientes.resources.v1 import mount_pagination
from cadastro_clientes.modules import client as cl
from cadastro_clientes.models.client import (
        InsertClientRequest, InsertClientResponse, CLIENT_DEFAULT_RESPONSE, LIST_FILTER_CLIENT_RESPONSE,
        ListFilterClientResponse, FindClientByIdResponse, FIND_CLIENT_BY_ID_RESPONSE, DeleteClientByIdResponse,
        DELETE_CLIENT_BY_ID_RESPONSE, DELETE_COLLECTION_RESPONSE, DeleteCollectionResponse
        )

router = APIRouter()


@router.post("/insert", response_model=InsertClientResponse, status_code=201,
             summary="Gravar um cliente no banco de dados", responses=CLIENT_DEFAULT_RESPONSE)
async def save_client(
    client_data: InsertClientRequest = Body(
        ...,
        example={
                "collection": "colecao",
                "client_type": "a",
                "gender": "m",
                "name": {
                    "title": "mr",
                    "first": "jose",
                    "last": "da silva"
                },
                "location": {
                    "region": "southwest",
                    "street": "rua",
                    "city": "São Paulo",
                    "state": "São Paulo",
                    "postcode": 11111,
                    "coordinates":
                        {
                            "latitude": "-57.654",
                            "longitude": "-986.1445"
                        },
                        "timezone": {
                            "offset": "-3:00",
                            "description": "America, São Paulo"
                        }
                },
                "email": "jose_da_silva@email.com",
                "picture": {
                    "large": "https://url/large.com.br",
                    "medium": "https://url/medium.com.br",
                    "thumbnail": "https://url/thumbnail.com.br"
                },
                "dob": {
                            "date": "1968-01-24T18:03:23Z",
                            "age": 50
                        },
                "phone": "(01) 5415-5648",
                "cell": "(10) 8264-5550",
                "birthday": "1979-01-22T03:35:31Z",
                "registered": {
                            "date": "2004-01-23T23:54:33Z",
                            "age": 14
                        },
                "telephone_numbers": [
                            "+556629637520"
                        ],
                "mobile_numbers": [
                            "+553270684089"
                        ],
                "nationality": "BR",
                "object_id_input": "111111111111"
            }
    ),
):
    """
    Endpoint para efetuar a gravação de um cliente de forma assíncrona no banco de dados. \
    Os dados do cliente foram abstraídos para que fosse possível a gravação antes (input) ou \
    depois do tratamento dos dados (output).
    """
    return {"result": [cl.insert(client_data.dict())]}


@router.get("/{collection}/{client_type}/{region}", status_code=200,
            summary="Lista os clientes a partir da região e do tipo",
            response_model=ListFilterClientResponse, responses=LIST_FILTER_CLIENT_RESPONSE)
def find_by_region_and_type(request: Request,
                            region: str = Query(..., description="Região do cliente"),
                            client_type: str = Query(..., description="Tipo do cliente"),
                            offset: int = Query(1, description="Página atual de retorno", gt=0),
                            qtd: int = Query(10, description="Quantidade de registros de retorno", gt=0),
                            collection: str = Query(None, description="Collection que o cliente(s) filtrado pertence")):
    """
    Filtrar um cliente por região e tipo, paginando o resultado
    """
    clients, total = cl.find_by_region_and_type(region, client_type, offset, qtd)
    return mount_pagination(clients, qtd, offset, total, str(request.url))


@router.get("/{collection}/{client_id}", status_code=200, summary="Busca o cliente a partir do id",
            response_model=FindClientByIdResponse, responses=FIND_CLIENT_BY_ID_RESPONSE)
def find_by_id(collection: str = Query(..., description="Coleção do cliente buscado"),
               client_id: str = Query(..., description="Id do cliente")):
    return {"result": cl.find_by_id(collection, client_id)}


@router.delete("/{collection}/{client_id}", status_code=200, summary="Deleta o cliente a partir do id",
               response_model=DeleteClientByIdResponse, responses=DELETE_CLIENT_BY_ID_RESPONSE)
def delete_by_id(collection: str = Query(..., description="Coleção do cliente"),
                 client_id: str = Query(..., description="Id do cliente")):
    return {"result": cl.delete_one(collection, client_id)}


@router.delete("/{collection}", status_code=200, summary="Deleta uma coleção",
               response_model=DeleteCollectionResponse, responses=DELETE_COLLECTION_RESPONSE)
def delete_collection(collection: str = Query(..., description="Coleção a ser deletada")):
    return {"result": cl.delete_collection(collection)}
