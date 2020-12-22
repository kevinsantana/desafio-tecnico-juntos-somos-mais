# Executando testes

Os testes da aplicação realizam a validação das respostas às requisições dos endpoints, validando o código de retorno esperado, o conteúdo do retorno e o tipo do retorno.

O ideal é que os testes sejam executados de forma _dockerizada_, para tanto,  é preciso que os _containers_ da API e do banco de dados estejam em execução, o que pode ser feito seguindo as instruções em [Instalação e Execução]().

Com o container da API nomeado como `cadastro`, execute:

``` bash
docker container exec -it cadastro pytest -v
```

ou, ainda, desde que se possua um banco de dados `mongoDB` em execução na sua máquina, e com as mesmas configurações do arquivo [mongo-init.js](./cadastro_clientes/script/mongo-init.js), é possível executar os testes através de um terminal no mesmo nível de pastas da pasta [cadastro_clientes](./cadastro_clientes), da seguinte maneira:

``` bash
pip3 install pytest
pytest -v
```
