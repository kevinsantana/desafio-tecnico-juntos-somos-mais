#!/bin/bash
docker rmi $(docker images -qf "dangling=true")
docker-compose -f cadastro.yml up -d