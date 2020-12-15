from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Field

from cadastro_clientes.models import (
    ObjectID, parse_openapi, Pagination, Message
    )


class ClientRegion(str, Enum):
    norte = "norte"
    nordeste = "nordeste"
    centro_oeste = "centro_oeste"
    sudeste = "sudeste"
    sul = "sul"


class ClientType(str, Enum):
    especial = "especial"
    normal = "normal"
    trabalhoso = "trabalhoso"


class Client(BaseModel):
    _id: ObjectID
    collection: str
    client_type: Optional[str]
    gender: str
    name: dict
    location: dict
    email: str
    picture: dict
    dob: Optional[dict]
    phone: Optional[str]
    cell: Optional[str]
    birthday: Optional[str]
    registered: Union[dict, str]
    telephone_numbers: Optional[list]
    mobile_numbers: Optional[list]
    nationality: Optional[str]
    object_id_input: Optional[str]


class InsertClientResponse(BaseModel):
    result: List[str] = Field(..., description="ObjectId do cliente inserido")


class ListFilterClientResponse(BaseModel):
    result: List[Client]
    pagination: Pagination = Field(..., description="Dados de paginação")


class FindClientByIdResponse(BaseModel):
    result: Client


class DeleteClientByIdResponse(BaseModel):
    result: bool


class DeleteCollectionResponse(BaseModel):
    result: bool


CLIENT_DEFAULT_RESPONSE = parse_openapi()
LIST_FILTER_CLIENT_RESPONSE = parse_openapi([
    Message(status=416, message="A combinação de filtros informada é inválida!",
            stacktrace="Traceback (most recent call last): ...")
])
FIND_CLIENT_BY_ID_RESPONSE = parse_openapi([
    Message(status=404, message="O id do cliente não foi encontrado",
            stacktrace="Traceback (most recent call last): ...")
])
DELETE_CLIENT_BY_ID_RESPONSE = parse_openapi([
    Message(status=404, message="O id do cliente não foi encontrado",
            stacktrace="Traceback (most recent call last): ...")
])
DELETE_COLLECTION_RESPONSE = parse_openapi([
    Message(status=404, message="A coleção informada não foi encontrada",
            stacktrace="Traceback (most recent call last): ...")
])
