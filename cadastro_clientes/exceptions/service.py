from cadastro_clientes.exceptions import ClientException


class ServiceException(ClientException):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = f"Erro ao efetuar a requisição: \n {message}"
        super().__init__(self.status_code, self.message)
