import os
import numpy as np


# MongoDB
MONGO_DB = os.environ.get("MONGO_DB", "cadastro")
MONGO_HOST = os.environ.get("MONGO_HOST", "db_cadastro")
MONGO_PASS = os.environ.get("MONGO_PASS", "1q2w3e")
MONGO_USR = os.environ.get("MONGO_USR", "cadastro")
MONGO_PORT = os.environ.get("MONGO_PORT", "27017")


# Aplicação
CLIENT_INPUT_URL = os.environ.get("CLIENT_INPUT_URL" ,"https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.json") #noqa
# CLIENT_INPUT_URL = os.environ.get("CLIENT_INPUT_URL", "https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.csv") #noqa
CLIENT_CLASSIFICATION = {
        "especial": {
            "latitude": np.linspace(-46.361_899, -34.276_938, 10_000),
            "longitude": np.linspace(-15.411_580, -2.196_998, 10_000)
        },
        "normal": {
            "latitude": np.linspace(-54.777_426, -46.603_598, 10_000),
            "longitude": np.linspace(-34.016_466, -26.155_681, 10_000)
        }
    }

ESTADOS_REGIOES = {
    'acre': 'norte',
    'alagoas': 'nordeste',
    'amapa': 'norte',
    'amazonas': 'norte',
    'bahia': 'nordeste',
    'ceara': 'nordeste',
    'distrito federal': 'centro oeste',
    'espirito santo': 'sudeste',
    'goias': 'centro oeste',
    'maranhao': 'nordeste',
    'mato grosso': 'centro oeste',
    'mato grosso do sul': 'centro oeste',
    'minas gerais': 'sudeste',
    'para': 'norte',
    'paraiba': 'nordeste',
    'parana': 'sul',
    'pernambuco': 'nordeste',
    'piaui': 'nordeste',
    'rio de janeiro': 'sudeste',
    'rio grande do norte': 'nordeste',
    'rio grande do sul': 'sul',
    'rondonia': 'norte',
    'roraima': 'norte',
    'santa catarina': 'sul',
    'sao paulo': 'sudeste',
    'sergipe': 'nordeste',
    'tocantins': 'norte'
    }

RE_ONLY_NUMBERS = "[^0-9]"
