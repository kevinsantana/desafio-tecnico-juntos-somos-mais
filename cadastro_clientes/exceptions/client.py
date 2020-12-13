from cadastro_clientes.exceptions import ClientException


class ClientNotFoundException(ClientException):
    def __init__(self, client_id: str):
        message = f"O id {client_id} do cliente não foi encontrado"
        super().__init__(404, message)


class FilterClientException(ClientException):
    def __init__(self, region: str = None, client_type: str = None):
        message = ""
        if region:
            message = "Região do cliente não informada"
        elif client_type:
            message = "Clasificação do cliente não informada"
        else:
            message = "A região e a classificação o cliente não foram informadas"
        super().__init__(416, message)


class ColllectionNotFoundException(ClientException):
    def __init__(self, collection: str):
        message = f"A coleção {collection} não foi encontrada ou não existe"
        super().__init__(404, message)
