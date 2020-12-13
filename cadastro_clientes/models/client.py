from typing import List, Optional

from pydantic import BaseModel, Field

from cadastro_clientes.models import (
    parse_openapi, DictOrStr, Pagination, Message
    )


class Register(BaseModel):
    registered: Optional[DictOrStr]


class InsertClientRequest(BaseModel):
    collection: str
    client_type: Optional[str] = None
    gender: str
    name: dict
    location: dict
    email: str
    picture: dict
    dob: Optional[dict] = None
    phone: Optional[str] = None
    cell: Optional[str] = None
    birthday: Optional[str] = None
    registered: Optional[DictOrStr] = None
    telephone_numbers: Optional[list] = None
    mobile_numbers: Optional[list] = None
    nationality: Optional[str] = None
    object_id_input: Optional[str] = None


class InsertClientResponse(BaseModel):
    result: List[str] = Field(..., description="ObjectId do cliente inserido")


class ListClientOutputResponse(BaseModel):
    client_type: str
    gender: str
    name: dict
    location: dict
    email: str
    birthday: str
    registered: str
    telephone_numbers: list
    mobile_numbers: list
    picture: dict
    nationality: str


class ListFilterClientResponse(BaseModel):
    result: List[ListClientOutputResponse]
    pagination: Pagination = Field(..., description="Dados de paginação")


class FindClientByIdResponse(BaseModel):
    result: InsertClientRequest = Field(..., description="Dados do cliente")


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
