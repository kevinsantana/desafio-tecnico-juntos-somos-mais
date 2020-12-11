from typing import List, Optional

from pydantic import BaseModel, Field

from cadastro_clientes.models import (
    parse_openapi, DictOrStr, StrOrNone, ListOrNone
    )


class Register(BaseModel):
    registered: Optional[DictOrStr] = None


class InsertClientRequest(BaseModel):
    collection: str
    type: StrOrNone = None
    gender: StrOrNone = None
    name: DictOrStr = None
    location: DictOrStr = None
    email: StrOrNone = None
    picture: DictOrStr = None
    dob: DictOrStr = None
    phone: StrOrNone = None
    cell: StrOrNone = None
    birthday: StrOrNone = None
    registered: DictOrStr = None
    telephone_numbers: ListOrNone = None
    mobile_numbers: ListOrNone = None
    nationality: StrOrNone = None
    object_id_input: StrOrNone = None


class InsertClientResponse(BaseModel):
    result: List[str] = Field(..., description="ObjectId do cliente inserido")


CLIENT_DEFAULT_RESPONSE = parse_openapi()
