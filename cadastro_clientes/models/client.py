from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Field

from cadastro_clientes.models import (
    parse_openapi, Pagination, Message
    )


class CustomBaseModel(BaseModel):
    def dict(self, **kwargs):
        hidden_fields = set(
            attribute_name
            for attribute_name, model_field in self.__fields__.items()
            if model_field.field_info.extra.get("hidden") is True
        )
        kwargs.setdefault("exclude", hidden_fields)
        return super().dict(**kwargs)


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


class ClientInsert(CustomBaseModel):
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

    class Config:
        schema_extra = {
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
                "object_id_input": "5fde23e3390e8a6f0591c457"
            }


class ClientShow(CustomBaseModel):
    id: Optional[str] = Field(alias="_id", hidden=True)
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
    result: List[ClientShow]
    pagination: Pagination = Field(..., description="Dados de paginação")


class FindClientByIdResponse(BaseModel):
    result: List[ClientShow]


class DeleteClientByIdResponse(BaseModel):
    result: List[bool]


class DeleteCollectionResponse(BaseModel):
    result: List[bool]


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
