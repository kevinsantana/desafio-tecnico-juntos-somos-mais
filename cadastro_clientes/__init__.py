__version__ = "0.1.5"

import time
import uuid
import urllib3
import traceback

from loguru import logger
from fastapi import FastAPI
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError

from cadastro_clientes.resources import v1
from cadastro_clientes.files import html_description
from cadastro_clientes.resources.v1 import doc_sphinx
from cadastro_clientes.exceptions import ClientException
from docs import build_html_pages, build_html_static, build_html_source

urllib3.disable_warnings()

logger.add("cadastro_clientes.log", rotation="500 MB")

logger.level("REQUEST RECEBIDA", no=38, color="<yellow>")
logger.level("REQUEST FINALIZADA", no=39, color="<green>")
logger.level("STATUS ALERT", no=42, color="<blue>")
logger.level("STATUS ERROR", no=500, color="<red>")


description = open(html_description).read()

app = FastAPI(
    title="DESAFIO TÉCNICO JUNTOS SOMOS MAIS - CADASTRO DE CLIENTES",
    description=description,
    version=__version__,
    docs_url="/v1/swagger",
    redoc_url="/v1/docs"
)

# versionamento rotas
app.include_router(v1, prefix="/v1")

# sphinx
app.include_router(doc_sphinx.router)
app.mount("/pages", StaticFiles(directory=build_html_pages), name="pages")
app.mount("/_static", StaticFiles(directory=build_html_static), name="static")
app.mount("/_sources", StaticFiles(directory=build_html_source), name="sources")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    id = uuid.uuid1()

    logger.log("REQUEST RECEBIDA", f"[{request.method}] ID: {id} - IP: {request.client.host}"
               + f" - ENDPOINT: {request.url.path}")

    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    logger.log("REQUEST FINALIZADA", f"[{request.method}] ID: {id} - IP: {request.client.host}"
               + f" - ENDPOINT: {request.url.path} - TEMPO: {process_time}")
    response.headers["X-Process-Time"] = str(process_time)

    return response


@app.exception_handler(ClientException)
async def camara_exception_handler(request: Request, exception: ClientException):
    return JSONResponse(
        status_code=exception.status_code,
        content={
            "status": exception.status_code,
            "mensagem": exception.message,
            "stacktrace": traceback.format_exc()
        }
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exception: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "status": 422,
            "mensagem": "Campo de requisição inválido",
            "stacktrace": traceback.format_exc()
        }
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exception: HTTPException):
    message = {404: "Endereço não encontrado", 405: "Método não permitido", 500: "Ocorreu um erro interno!"}
    return JSONResponse(
        status_code=exception.status_code,
        content={
            "status": exception.status_code,
            "mensagem": message[exception.status_code],
            "stacktrace": traceback.format_exc()
        }
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"]
)
