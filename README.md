# cadastro-clientes

Cadastro de clientes é um microsserviço para manter clientes através de arquivo(s) `JSON` e/ou `CSV`.

A aplicação foi construída em uma arquitetura de [microsserviço](https://martinfowler.com/articles/microservices.html), em que cada container compõe um parte do todo, são eles:

* `db_cadastro`: É o banco de dados MongoDB responsável por manter o cadastro dos clientes;
* `etl_clientes`: É quem faz a carga no banco de dados a partir de um arquivo `CSV` ou `JSON` via requisição http;
* `cadastro-clientes`: É a API que expõe e permite a manipulação dos clientes.

A solução executa um pré-tratamento dos dados, classifica os clientes e persiste os dados em banco de dados. Permitindo que os clientes sejam recuperados por meio da região do usuário e seu tipo de classificação.

A API foi construída com [FastApi](https://fastapi.tiangolo.com/), que possuí uma excelente validação de tipos, tanto de entrada como de saída da API, usando [Pydantic](https://pydantic-docs.helpmanual.io/). Além disso `FastApi` documenta automaticamente a API utlizando [OpenAPI](https://github.com/OAI/OpenAPI-Specification).

## Prerequisites

É preciso configurar o [docker](https://docs.docker.com/) e o [docker-compose](https://docs.docker.com/compose/) para consumir o projeto.

As variáveis de ambiente utilizadas pelos containers estão configuradas no arquivo [cadastro.yml](cadastro.yml), e são exatamente as mesmas configuradas no arquivo [config.py](cadastro_clientes/config.py) que contém os dados para conexão com o banco de dados através do [Pymongo](https://pymongo.readthedocs.io/en/stable/).

### Instalação e Execução

A execução da aplicação é dividida em duas partes: `build` das imagens consumidas pelos containers e a execução dos containers. Para o [build](./build.sh) das imagens é necessário executar o seguinte comando:

```bash
bash build.sh
```

Com as imagens _buildadas_ é possível executar os containers, através do comando:

```bash
bash run.sh
```

Com a aplicação no ar, basta acessar o [ReDoc](http://localhost:7000/v1/docs) para saber como utilizar cada um dos *endpoints* e para utilizar os *endpoints* acesse o [Swagger](http://localhost:7000/v1/swagger).

Antes de iniciar a aplicação, verifique se a base de dados foi carregada conferindo os _logs_ do container `etl_clientes`, através do comando:

```bash
docker container logs -f etl_clientes
```

Além de poder verificar a quantidade e o andamento da carga da base de dados é possível verificar se o status da aplicação está em `Ready`, dessa maneira é possível consumir os _endpoints_.

## Executando testes

Os testes da aplicação realizam a validação das respostas às requisições dos endpoints, validando o código de retorno esperado, o conteúdo do retorno e o tipo do retorno.

O ideal é que os testes sejam executados de forma _dockerizada_, para tanto,  é preciso que os _containers_ da API e do banco de dados estejam em execução, o que pode ser feito seguindo as instruções em [Instalação e Execução]().

Com o container da API nomeado como `cadastro`, execute:

```bash
docker container exec -it cadastro pytest -v
```

### Estilo de código

Esse código segue o padrão PEP8 e pode ser testado com a biblioteca [PyLama](https://github.com/klen/pylama) como no exemplo a seguir

```bash
pip3 install pylama
pylama -o pylama.ini .
```

## Deploy

Com a aplicação _dockerizada_ e testada, é possível efetuar o _deploy_ em um orquestrador de _containers_ a exemplo do [Kubernetes](https://kubernetes.io/pt/), ou mesmo, com o orquestrador nativo do Docker [Swarm](https://docs.docker.com/engine/swarm/).

## Construído Com

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
