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