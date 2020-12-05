import os


# Postgres
PGSQL_DB = os.environ.get("PGSQL_DB", "cadastro_cliente_input")
PGSQL_HOST = os.environ.get("PGSQL_HOST", "db_cadastro_input")
PGSQL_PASS = os.environ.get("PGSQL_PASS", "1q2w3e")
PGSQL_USR = os.environ.get("PGSQL_USR", "cadastro")
PGSQL_PORT = os.environ.get("PGSQL_PORT", "5432")

# MongoDB
MONGO_DB = os.environ.get("MONGO_DB", "cadastro_cliente_output_db")
MONGO_HOST = os.environ.get("MONGO_HOST", "db_cadastro_output")
MONGO_PASS = os.environ.get("MONGO_PASS", "1q2w3e")
MONGO_USR = os.environ.get("MONGO_USR", "cadastro")
MONGO_PORT = os.environ.get("MONGO_PORT", "27017")
