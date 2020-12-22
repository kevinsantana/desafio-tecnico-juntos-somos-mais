import pymongo
from bson import ObjectId

from cadastro_clientes.database import Database


class Client(Database):
    def __init__(self, _id: str = None, gender: str = None, name: dict = None,
                 location: dict = None, email: str = None, picture: dict = None,
                 dob: dict = None, registered=None, phone: str = None,
                 cell: str = None, client_type: str = None, birthday: float = None,
                 telephone_numbers: list = None, mobile_numbers: list = None,
                 nationality: str = None, object_id_input: str = None):
        self.__id = _id
        self.__gender = gender
        self.__name = name
        self.__location = location
        self.__email = email
        self.__picture = picture
        self.__dob = dob
        self.__registered = registered
        self.__phone = phone
        self.__cell = cell
        self.__client_type = client_type
        self.__birthday = birthday
        self.__telephone_numbers = telephone_numbers
        self.__mobile_numbers = mobile_numbers
        self.__nationality = nationality
        self.__object_id_input = object_id_input

    @property
    def id(self):
        return str(self.__id)

    @property
    def gender(self):
        return self.__gender

    @property
    def name(self):
        return self.__name

    @property
    def location(self):
        return self.__location

    @property
    def email(self):
        return self.__email

    @property
    def picture(self):
        return self.__picture

    @property
    def dob(self):
        return self.__dob

    @property
    def registered(self):
        return self.__registered

    @property
    def phone(self):
        return self.__phone

    @property
    def cell(self):
        return self.__cell

    @property
    def client_type(self):
        return self.__type

    @property
    def birthday(self):
        return self.__birthday

    @property
    def telephone_numbers(self):
        return self.__telephone_numbers

    @property
    def mobile_numbers(self):
        return self.__mobile_numbers

    @property
    def nationality(self):
        return self.__nationality

    @property
    def object_id_input(self):
        return str(self.__object_id_input)

    @object_id_input.setter
    def object_id_input(self, object_id: str):
        if isinstance(object_id, str):
            self.__object_id_input = ObjectId(object_id)

    def dict(self) -> dict:
        new_dict = dict()
        for key, value in self.__dict__.items():
            if value and key != "_Client__id":
                new_dict[key.replace("_Client__", "")] = value
            elif value and key == "_Client__id":
                new_dict[key.replace("_Client_", "")] = value
        return new_dict

    def insert(self, collection: str):
        if self.__object_id_input:
            self.object_id_input = self.object_id_input
        document_id = super().insert(collection=collection, document=self.dict())
        return document_id

    def find_by_region_and_type(self, region: str, client_type: str, collection: str,
                                offset: int = 0, qtd: int = 10):
        sort_options = [("$natural", pymongo.ASCENDING)]
        query = {"location.region": region, "client_type": client_type}
        documents, total = super().find_all(collection=collection,
                                            sort_options=sort_options,
                                            offset=offset, qtd=qtd,
                                            filter=query)
        clients = [Client(**document).dict() for document in documents]
        return clients, total

    def find_by_id(self, collection: str, client_id: str):
        sort_options = [("$natural", pymongo.ASCENDING)]
        query = {"_id": ObjectId(client_id)}
        return super().find_one(collection=collection, filter=query, sort_options=sort_options)

    def delete_one(self, collection: str, client_id: str):
        query = {"_id": ObjectId(client_id)}
        return super().delete_one(collection=collection, filter=query)

    def delete_collection(self, collection: str):
        return super().delete_collection(collection=collection)

    def __repr__(self):
        return f"{self.__dict__.items()}"
