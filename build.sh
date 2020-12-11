#!/bin/bash
docker-compose -f cadastro.yml build \
--build-arg MONGO_DB=${MONGO_DB} \
--build-arg MONGO_HOST=${MONGO_HOST} \
--build-arg MONGO_PASS=${MONGO_PASS} \
--build-arg MONGO_USR=${MONGO_USR} \
--build-arg MONGO_PORT=${MONGO_PORT} \
--force-rm --no-cache