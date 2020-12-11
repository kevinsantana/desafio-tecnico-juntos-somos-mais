from cadastro_clientes.database.client import Client


def __client_to_dict(obj: Client) -> dict:
    return {key.replace("_Client__", ""): value for key, value in obj.items() if value}


def insert(client_data: dict) -> dict:
    """
    Insere um cliente no banco de dados.

    :param client_data: Dicionário com as informações do cliente
    :type client_data: dict
    :return: objectid do documento gravado
    :rtype: str
    """
    client_id = Client(client_data["collection"]).insert(__client_to_dict(client_data))
    return str(client_id)
