# Instalação e Execução

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
