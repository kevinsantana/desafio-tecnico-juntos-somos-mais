from fastapi.testclient import TestClient

from cadastro_clientes import app

client = TestClient(app)
