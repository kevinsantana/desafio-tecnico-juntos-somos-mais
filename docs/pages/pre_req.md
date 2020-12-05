### Prerequisites

Sugere-se a criação de um ambiente virtual para instalação das dependências da aplicação, como por exemplo o [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).

Para instalar as dependências do projeto, execute:

```
pip3 install -e .
```

É preciso, também, ter o [docker](https://docs.docker.com/) e o [docker-compose](https://docs.docker.com/compose/) instalados. As variáveis de ambiente listadas abaixo devem estar exportadas no terminal para o funcionamento da aplicação. Enquanto o valor das variáveis mudam conforme a necessidade de execução, os nomes devem permanecer os mesmos, são eles:

* `MONGO_INITDB_ROOT_USERNAME`: _Username_ criado no momento de execução do container;
* `MONGO_INITDB_ROOT_PASSWORD`: _Password_ criado no momento de execução do container;
* `MONGO_INITDB_DATABASE`: _database_ criado no momento de execução do container;

* `MONGO_DB`: Nome do mongodb para armazenamento dos dados de output;
* `MONGO_HOST`: _Hostname_ do mongodb;
* `MONGO_PASS`: Senha do mongodb para armazenamento dos dados de output;
* `MONGO_USR`: Usuário do mongodb para armazenamento dos dados de output;
* `MONGO_PORT`: Porta do mongodb para armazenamento dos dados de output;

* `POSTGRES_DB`: _database_ criado no momento de execução do container;
* `POSTGRES_USER`: _Username_ criado no momento de execução do container;
* `POSTGRES_PASSWORD`: _Password_ criado no momento de execução do container;

* `PGSQL_DB`: Nome do postgres para armazenamento dos dados de input;
* `PGSQL_HOST`: _Hostname_ do postgres;
* `PGSQL_PASS`: Senha do postgres para armazenamento dos dados de input;
* `PGSQL_USR`: Usuário do postgres para armazenamento dos dados de input;
* `PGSQL_PORT`: Porta do postgres para armazenamento dos dados de input;

* `PGADMIN_DEFAULT_EMAIL`: Email para login no pgAdmin, necessário para execução do container.
* `PGADMIN_DEFAULT_PASSWORD`: Senha para login no pgAdmin, necessário para execução do container.
