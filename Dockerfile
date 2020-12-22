FROM centos/python-38-centos7

USER root

ENV MONGO_DB="$MONGO_DB"
ENV MONGO_HOST="$MONGO_HOST"
ENV MONGO_PASS="$MONGO_PASS"
ENV MONGO_USR="$MONGO_USR"
ENV MONGO_PORT="$MONGO_PORT"

# DEPENDENCIES
RUN yum install -y \
        poppler-utils

RUN yum clean all

# INSTALL APPLICATION
COPY ./cadastro_clientes /deploy/cadastro_clientes
COPY ./docs /deploy/docs
COPY setup.py /deploy
COPY README.md /deploy
COPY /tests /deploy/tests

WORKDIR /deploy

RUN pip install -e .
RUN pip install pytest
