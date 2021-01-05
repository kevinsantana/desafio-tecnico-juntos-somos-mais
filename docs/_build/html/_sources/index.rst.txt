Bem vindo à documentação do Cadastro de Clientes!
=================================================
Cadastro de clientes é um microsserviço para manter clientes através de arquivo(s) `JSON` e/ou `CSV`.


Introdução
===========
A aplicação foi construída em uma arquitetura de `Microsserviço <https://martinfowler.com/articles/microservices.html>`_,
em que cada container compõe um parte do todo, são eles:

* `db_cadastro`: É o banco de dados MongoDB responsável por manter o cadastro dos clientes;
* `etl_clientes`: É quem faz a carga no banco de dados a partir de um arquivo `CSV` ou `JSON` via requisição http;
* `cadastro-clientes`: É a API que expõe e permite a manipulação dos clientes.

A solução executa um pré-tratamento dos dados, classifica os clientes e persiste os dados em banco de dados. Permitindo que
os clientes sejam recuperados por meio da região do usuário e seu tipo de classificação.

A API foi construída com `FastApi <https://fastapi.tiangolo.com/)>`_, que possuí uma excelente validação de tipos,
tanto de entrada como de saída da API, usando `Pydantic <https://pydantic-docs.helpmanual.io/>`_.
Além disso `FastApi` documenta automaticamente a API utlizando `OpenAPI https://github.com/OAI/OpenAPI-Specification>`_.


Links
=====

`Github <https://github.com/kevinsantana/desafio-tecnico-juntos-somos-mais>`_

`Documentação da API <localhost:7000/v1/swagger>`_


.. toctree::
   :maxdepth: 1
   :caption: Documentação básica
   :titlesonly:

   /pages/pre_req.md
   /pages/installation.md
   /pages/tests.md
   /pages/made_with.md
   /pages/deploy.md


.. toctree::
   :maxdepth: 2
   :caption: Documentação do Código

   /pages/modules
   /pages/database
   /pages/script



Tabelas e Índices
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
