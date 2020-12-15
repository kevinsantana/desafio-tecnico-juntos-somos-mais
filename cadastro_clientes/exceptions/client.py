from cadastro_clientes.exceptions import ClientException


class ClientNotFoundException(ClientException):
    def __init__(self, status_code: int, client_id: str):
        self.status_code = status_code
        self.message = f"O id {client_id} do cliente não foi encontrado"
        super().__init__(status_code, self.message)


class FilterClientException(ClientException):
    def __init__(self, status_code: int, region: str = None, client_type: str = None):
        self.status_code = status_code
        self.message = ""
        if region:
            self.message = "Região do cliente não informada"
        elif client_type:
            self.message = "Clasificação do cliente não informada"
        else:
            self.message = "A região e a classificação o cliente não foram informadas"
        super().__init__(status_code, self.message)


class ColllectionNotFoundException(ClientException):
    def __init__(self, status_code: int, collection: str):
        self.status_code = status_code
        self.message = f"A coleção {collection} não foi encontrada ou não existe"
        super().__init__(status_code, self.message)
