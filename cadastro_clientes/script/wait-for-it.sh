#!/bin/bash
while ! nc -vn cadastro_clientes 5333; do sleep 60; done
bash /deploy/up.sh