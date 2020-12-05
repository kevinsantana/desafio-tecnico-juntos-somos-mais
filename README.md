# cadastro-clientes

Cadastro de clientes é um microsserviço para manter clientes através de arquivo(s) `JSON` e/ou `CSV`.

A solução executa um pré-tratamento dos dados, classifica os clientes e persiste os dados em banco de dados. Permitindo que os clientes sejam recuperados por meio da região do usuário e seu tipo de classificação.

A API foi construída com [FastApi](https://fastapi.tiangolo.com/), que possuí uma excelente validação de tipos, tanto de entrada como de saída da API, usando [Pydantic](https://pydantic-docs.helpmanual.io/). Além disso `FastApi` documenta automaticamente a API utlizando [OpenAPI](https://github.com/OAI/OpenAPI-Specification).

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

### Instalação e Execução

A execução da aplicação é dividida em duas partes: `build` das imagens consumidas pelos containers e a execução dos containers. Para o [build](./build.sh) das imagens é necessário executar o seguinte comando:

```
bash build.sh
```

Com as imagens _buildadas_ é possível executar os containers, através do comando:

```
bash run.sh
```

Com a aplicação no ar, basta acessar o [ReDoc](http://localhost:7000/v1/docs) para saber como utilizar cada um dos *endpoints* e para utilizar os *endpoints* acesse o [Swagger](http://localhost:7000/v1/swagger).

## Executando testes

Os testes da aplicação realizam a validação das respostas as requisições dos endpoints e a comunicação com outras soluções que compõem esta aplicação.

É possível executar os testes de forma _dockerizada_ conforme instruções abaixo:

```
docker container exec -it cadastro_clientes pytest
```

ou, ainda, através de um terminal no mesmo nível de pastas da pasta [cadastro_clientes](./cadastro_clientes), sem a execução da aplicação dentro de um _container_, da seguinte maneira

```
pip3 install pytest
pytest
```

### Estilo de código

Esse código segue o padrão PEP8 e pode ser testado com a biblioteca [PyLama](https://github.com/klen/pylama) como no exemplo a seguir

```
pip3 install pylama
pylama -o pylama.ini .
```

## Deploy

O deploy pode ser feito...

## Ferramentas

* [loguru](https://github.com/Delgan/loguru)
* [pydantic](https://pydantic-docs.helpmanual.io)
* [fastapi](https://fastapi.tiangolo.com)
* [uvicorn](https://www.uvicorn.org)
* [gunicorn](https://gunicorn.org)
* [requests](https://requests.readthedocs.io/en/master/)
* [sphinx](https://www.sphinx-doc.org/en/master/)

## Versionamento

O versionamento segue o padrão do [Versionamento Semântico](http://semver.org/). Para saber as versões de repositório entre nas [tags](https://github.com/kevinsantana/desafio-tecnico-juntos-somos-mais/-/tags).

## License

Todos os direitos são reservados ao autor Kevin de Santana Araujo.

## Outras informações

* Caso tenha alguma dúvida em relação ao projeto, ou queira contribuir com sugestões ou críticas, abra uma [issue]() ou procure o desenvolvedor através do email kevin_santana.araujo@hotmail.com
