from bson import ObjectId


from cadastro_clientes.database import Database


class Client(Database):
    def __init__(self, collection: str, _id: str = None, gender: str = None, name: dict = None,
                 location: dict = None, email: str = None, picture: dict = None,
                 dob: dict = None, registered=None, phone: str = None,
                 cell: str = None, type: str = None, birthday: float = None,
                 telephone_numbers: list = None, mobile_numbers: list = None,
                 nationality: str = None, object_id_input: str = None):
        self.__id = ObjectId(_id)
        self.__collection = collection
        self.__gender = gender
        self.__name = name
        self.__location = location
        self.__email = email
        self.__picture = picture
        self.__dob = dob
        self.__registered = registered
        self.__phone = phone
        self.__cell = cell
        self.__type = type
        self.__birthday = birthday
        self.__telephone_numbers = telephone_numbers
        self.__mobile_numbers = mobile_numbers
        self.__nationality = nationality
        self.__object_id_input = object_id_input

    @property
    def id(self):
        return str(self.__id)

    @id.setter
    def id(self, model_id: str):
        self.__id = ObjectId(model_id)

    @property
    def collection(self):
        return self.__collection

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
    def type(self):
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
        return self.__object_id_input

    def insert(self, document: dict):
        document["_id"] = ObjectId(super().insert(collection=self.__collection, document=document))
        return document["_id"]

    def find_all():
        pass

    def find_by_id():
        pass

    def update():
        pass

    def dict(self) -> dict:
        return {key.replace("_Client__", ""): value for key, value in self.__dict__.items() if value}

    def __repr__(self):
        return f"{self.__dict__.items()}"
