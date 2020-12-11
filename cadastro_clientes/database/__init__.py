import abc

from pymongo import MongoClient

from loguru import logger

from cadastro_clientes.config import (
    MONGO_DB, MONGO_HOST, MONGO_PASS, MONGO_PORT, MONGO_USR
    )


class Database:
    def __connect(self):
        self.__connection = MongoClient(f"mongodb://{MONGO_USR}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}")
        self.__db = self.__connection.get_database()

    def __disconnect(self):
        self.__connection.close()

    def insert(self, collection: str, document: dict) -> str:
        """
        Insere um documento em uma coleção.

        :param collection: Nome da collection onde o documento será inserido
        :type collection: str
        :param document: documento a ser inserido
        :type document: dict
        :return: id gerado
        :rtype: str
        """
        self.__connect()
        document_id = str(self.__db[collection].insert_one(document).inserted_id)
        self.__disconnect()
        return document_id

    def find_all(self, collection: str, fields: list = [], sort_options: list = [],
                 offset: int = 0, qtd: int = 0, filter: list = None) -> tuple:
        """
        Recupera todos os documentos de uma collection

        :param collection: nome da collection
        :type collection: str
        :param fields: Lista de campos no resultado
        :type fields: list
        :param sort_options: Opções de ordenação
        :type sort_options: list
        :param offset: Quantidade de informações que devem ser puladas
        :type offset: int
        :param qtd: Limite de informações no resultado
        :type qtd: int
        :param filter: Query para filtrar elementos
        :type filter: list
        :return: tupla com documentos da collection e total de documentos
        :rtype: tuple
        """
        self.__connect()
        projection = {field: 1 for field in fields}
        documents = self.__db[collection].find(filter=filter, projection=projection)
        total = documents.count()
        documents = documents.sort(sort_options).skip(offset).limit(qtd)
        self.__disconnect()
        return documents, total

    def find(self, collection: str, filter: dict, sort_options: list = []):
        """
        Busca um documento

        :param collection: Nome da coleção
        :type collection: str
        :param filter: Query para filtrar elementos
        :type filter: dict
        :param sort_options: Opções de ordenação
        :type sort_options: list
        :return: documento encontrado
        :rtype: dict
        """
        self.__connect()
        document = self.__db[collection].find_one(filter=filter, sort=sort_options)
        self.__disconnect()
        return document

    def update(self, collection: str, query: str, values: str):
        """
        Atualiza um documento

        :param collection: nome da collection
        :type collection: str
        :param query: Query para filtrar elementos
        :type query: str
        :param values: valores a serem atualizados
        :type values: str
        """
        self.__connect()
        logger.debug([collection, query, values])
        self.__db[collection].update_one(query, {"$set": values})
        self.__disconnect()

    def get_collections(self):
        """
        Recupera as coleções do banco de dados

        :return: coleções
        :rtype: dict
        """
        self.__connect()
        collections = self.__db.list_collection_names()
        self.__disconnect()
        return collections

    @abc.abstractclassmethod
    def dict(self):
        raise NotImplementedError
