class CadastroClientesException(Exception):
    def __init__(self, status: int, message: str):
        self.status_code = status
        self.mensagem = message
