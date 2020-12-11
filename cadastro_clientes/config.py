import os


# MongoDB
MONGO_DB = os.environ.get("MONGO_DB", "cadastro")
MONGO_HOST = os.environ.get("MONGO_HOST", "db_cadastro")
MONGO_PASS = os.environ.get("MONGO_PASS", "1q2w3e")
MONGO_USR = os.environ.get("MONGO_USR", "cadastro")
MONGO_PORT = os.environ.get("MONGO_PORT", "27017")
