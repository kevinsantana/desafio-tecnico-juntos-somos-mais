from fastapi import APIRouter, Body, Request, Query, Path

from cadastro_clientes.modules import client as cl
from cadastro_clientes.resources.v1 import mount_pagination
from cadastro_clientes.models.client import InsertClientResponse, CLIENT_DEFAULT_RESPONSE
from cadastro_clientes.models.client import ClientInsert, ClientShow, ClientRegion, ClientType
from cadastro_clientes.models.client import FindClientByIdResponse, FIND_CLIENT_BY_ID_RESPONSE
from cadastro_clientes.models.client import DeleteCollectionResponse, DELETE_COLLECTION_RESPONSE
from cadastro_clientes.models.client import ListFilterClientResponse, LIST_FILTER_CLIENT_RESPONSE
from cadastro_clientes.models.client import DeleteClientByIdResponse, DELETE_CLIENT_BY_ID_RESPONSE


router = APIRouter()


@router.post("/{collection}/insert", response_model=InsertClientResponse, status_code=201,
             summary="Gravar um cliente no banco de dados", responses=CLIENT_DEFAULT_RESPONSE)
def save_client(collection: str = Path(..., description="Collection que o cliente será inserido"),
                client_data: ClientInsert = Body(..., example=ClientInsert.Config.schema_extra)):
    """
    Endpoint para efetuar a gravação de um cliente no banco de dados. Os dados \
    do cliente foram abstraídos para que fosse possível a gravação antes (input) ou \
    depois do tratamento dos dados (output).
    """
    return {"result": [cl.insert(client_data.dict(by_alias=True), collection=collection)]}


@router.get("/{collection}/{client_type}/{region}", status_code=200,
            summary="Lista os clientes a partir da região e do tipo",
            response_model=ListFilterClientResponse, responses=LIST_FILTER_CLIENT_RESPONSE,
            response_model_exclude_none=True)
def find_by_region_and_type(request: Request,
                            region: ClientRegion = Path(..., description="Região do cliente"),
                            client_type: ClientType = Path(..., description="Tipo do cliente"),
                            offset: int = Query(1, description="Página atual de retorno", gt=0),
                            qtd: int = Query(10, description="Quantidade de registros de retorno", gt=0),
                            collection: str = Path(None, description="Collection que o cliente(s) filtrado pertence")):
    """
    Filtrar um cliente por região e tipo, paginando o resultado
    """
    clients, total = cl.find_by_region_and_type(region=region, client_type=client_type,
                                                offset=offset, qtd=qtd, collection=collection)
    filtered_client_fields = [ClientShow(**client).dict(exclude={"id"}) for client in clients]
    return mount_pagination(filtered_client_fields, qtd, offset, total, str(request.url))


@router.get("/{collection}/{client_id}", status_code=200, summary="Busca o cliente a partir do id",
            response_model=FindClientByIdResponse, responses=FIND_CLIENT_BY_ID_RESPONSE,
            response_model_exclude_none=True)
def find_by_id(collection: str = Path(..., description="Coleção do cliente buscado"),
               client_id: str = Path(..., description="Id do cliente")):
    return {"result": [ClientShow(**cl.find_by_id(collection=collection, client_id=client_id)).dict(exclude={"id"})]}


@router.delete("/{collection}/{client_id}", status_code=200, summary="Deleta o cliente a partir do id",
               response_model=DeleteClientByIdResponse, responses=DELETE_CLIENT_BY_ID_RESPONSE)
def delete_by_id(collection: str = Path(..., description="Coleção do cliente"),
                 client_id: str = Path(..., description="Id do cliente")):
    return {"result": [cl.delete_one(collection=collection, client_id=client_id)]}


@router.delete("/{collection}", status_code=200, summary="Deleta uma coleção",
               response_model=DeleteCollectionResponse, responses=DELETE_COLLECTION_RESPONSE)
def delete_collection(collection: str = Path(..., description="Coleção a ser deletada")):
    return {"result": [cl.delete_collection(collection=collection)]}
