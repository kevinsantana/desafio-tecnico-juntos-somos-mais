FROM python:3.8-alpine3.12

# ENV VARS
ARG PGSQL_DB
ARG PGSQL_HOST
ARG PGSQL_PASS
ARG PGSQL_USR
ARG PGSQL_PORT
ARG MONGO_DB
ARG MONGO_HOST
ARG MONGO_PASS
ARG MONGO_USR
ARG MONGO_PORT

ENV PGSQL_DB="$PGSQL_DB"
ENV PGSQL_HOST="$PGSQL_HOST"
ENV PGSQL_PASS="$PGSQL_PASS"
ENV PGSQL_USR="$PGSQL_USR"
ENV PGSQL_PORT="$PGSQL_PORT"
ENV MONGO_DB="$MONGO_DB"
ENV MONGO_HOST="$MONGO_HOST"
ENV MONGO_PASS="$MONGO_PASS"
ENV MONGO_USR="$MONGO_USR"
ENV MONGO_PORT="$MONGO_PORT"

RUN apk add build-base \
    && apk add postgresql-dev --no-cache \
    && apk add poppler-utils --no-cache

COPY ./cadastro_clientes /deploy/cadastro_clientes
COPY ./docs /deploy/docs
COPY setup.py /deploy
COPY README.md /deploy
COPY /tests /deploy/tests

WORKDIR /deploy

RUN pip install -e .
RUN pip install pytest

EXPOSE 7000
CMD ["gunicorn", "--bind=0.0.0.0:7000", "--workers=3", "--worker-class=uvicorn.workers.UvicornWorker", "--timeout=174000", "cadastro_clientes:app"]
