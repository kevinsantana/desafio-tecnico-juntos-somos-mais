from cadastro_clientes.database.client import Client
from cadastro_clientes.exceptions.client import (
    ClientNotFoundException, ColllectionNotFoundException, FilterClientException
    )


def _objectId_to_str(client: dict):
    client.update({"_id": str(client.get("_id")),
                   "object_id_input": str(client.get("object_id_input"))
                   if client.get("object_id_input") else None})
    return client


def insert(client_data: dict, collection: str) -> dict:
    """
    Insere um cliente no banco de dados.

    :param client_data: Dicionário com as informações do cliente
    :type client_data: dict
    :return: ObjectId do documento gravado
    :rtype: str
    """
    return Client(**client_data).insert(collection=collection)


def find_by_region_and_type(region: str, client_type: str, offset: str, qtd: str,
                            collection: str = "output") -> list:
    """
    Retorna a lista com todos os clientes do tipo e região informados, de forma paginada

    :param region: Região dos clientes buscados
    :type region: str
    :param client_type: Tipo da classificação dos clientes buscados
    :type client_type: str
    :param offset: Página da resposta
    :type offset: str
    :param qtd: Quantidade de elementos por página
    :type qtd: str
    :return: Lista com os clientes encontrados em formato de dicionário
    :rtype: list
    :raises FilterClientException: Caso não sejam informados região e classificação do cliente
    """
    if not region and not client_type:
        raise FilterClientException(416, region=region, client_type=client_type)
    clients, total = Client().find_by_region_and_type(region=region, client_type=client_type,
                                                      qtd=qtd, offset=offset-1,
                                                      collection=collection)
    return [_objectId_to_str(client) for client in clients], total


def find_by_id(collection: str, client_id: str):
    """
    Retorna o cliente a partir do id informado.

    :param collection: Collection do cliente buscado
    :type collection: str
    :param client_id: Id do cliente buscado
    :type client_id: str
    :return: Cliente encontrado
    :rtype: dict
    :raises ClientNotFoundException: Caso o cliente informado não seja encontrado
    """
    client = Client().find_by_id(collection=collection, client_id=client_id)
    if not client:
        raise ClientNotFoundException(404, client_id)
    client = _objectId_to_str(client)
    return client


def delete_one(collection: str, client_id: str):
    """
    Deleta o cliente na collection informada.

    :param collection: Collection do cliente buscado
    :type collection: str
    :param client_id: Id do monogobd do cliente buscado
    :type client_id: str
    :return: True se o cliente foi deletado com sucesso, False caso contrário
    :rtype: boolean
    :raises ClientNotFoundException: Se o cliente informado não foi encontrado
    """
    if Client().delete_one(collection=collection, client_id=client_id):
        return True
    else:
        raise ClientNotFoundException(404, client_id)


def delete_collection(collection: str):
    """
    Deleta uma collection.

    :param collection: Collection do cliente buscado
    :type collection: str
    :return: True se a collection foi deletada com sucesso, False caso contrário
    :rtype: boolean
    :raises ColllectionNotFoundException: Collection informada não foi encontrada
    """
    if Client().delete_collection(collection=collection):
        return True
    else:
        ColllectionNotFoundException(404, collection)
