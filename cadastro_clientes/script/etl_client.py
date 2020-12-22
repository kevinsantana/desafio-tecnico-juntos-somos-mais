import re
import unicodedata
from collections import defaultdict, namedtuple

import requests
import pandas as pd
from loguru import logger

from cadastro_clientes.modules.client import insert
from cadastro_clientes.exceptions.service import ServiceException
from cadastro_clientes.config import (
    CLIENT_INPUT_URL, CLIENT_CLASSIFICATION, ESTADOS_REGIOES, RE_ONLY_NUMBERS
    )


def csv_to_dict(url: str) -> dict:
    """
    Transforma um arquivo csv em um dicionário do python, com o auxílio da biblioteca \
    pandas.

    :param str url: Url contendo o arquivo csv.
    :return: Dicionário contendo uma lista em que cada indíce é um registro do arquivo csv.
    :rtype: dict
    """
    dict_from_csv = pd.DataFrame(pd.read_csv(url, sep=",", header=0, index_col=False, quotechar='"')).to_dict("records")
    clients = defaultdict(list)
    for dict_record in dict_from_csv:
        Client = namedtuple("Client", list(dict_record.keys()))
        client = dict()
        client_fields = Client(*list(dict_record.values()))
        client["gender"] = client_fields.gender
        client["name"] = {}
        client["name"]["title"] = client_fields.name__title
        client["name"]["first"] = client_fields.name__first
        client["name"]["last"] = client_fields.name__last
        client["location"] = {}
        client["location"]["street"] = client_fields.location__street
        client["location"]["city"] = client_fields.location__city
        client["location"]["state"] = client_fields.location__state
        client["location"]["postcode"] = client_fields.location__postcode
        client["location"]["coordinates"] = {}
        client["location"]["coordinates"]["latitude"] = str(client_fields.location__coordinates__latitude)
        client["location"]["coordinates"]["longitude"] = str(client_fields.location__coordinates__longitude)
        client["location"]["timezone"] = {}
        client["location"]["timezone"]["offset"] = client_fields.location__timezone__offset
        client["location"]["timezone"]["description"] = client_fields.location__timezone__description
        client["email"] = client_fields.email
        client["dob"] = {}
        client["dob"]["date"] = client_fields.dob__date
        client["dob"]["age"] = client_fields.dob__age
        client["registered"] = {}
        client["registered"]["date"] = client_fields.registered__date
        client["registered"]["age"] = client_fields.registered__age
        client["phone"] = client_fields.phone
        client["cell"] = client_fields.cell
        client["picture"] = {}
        client["picture"]["large"] = client_fields.picture__large
        client["picture"]["medium"] = client_fields.picture__medium
        client["picture"]["thumbnail"] = client_fields.picture__thumbnail
        clients["results"].append(client)
    return clients


def strip_accents(word: str) -> str:
    """
    Função auxiliar para retirar acentos ortográficos da língua portuguesa de uma \
    palavra.

    :param str word: Palavra a ser limpa.
    :return: Palavra sem acentos.
    :rtype: str
    """
    try:
        word = unicode(word, "utf-8")
    except (TypeError, NameError):
        pass
    word = unicodedata.normalize("NFD", word)
    word = word.encode("ascii", "ignore")
    word = word.decode("utf-8")
    return str(word).lower()


def classify_client(latitude: float, longitude: float) -> str:
    """
    Classifica um cliente de acordo com a latitude e a longitude. Utiliza-se a \
    biblioteca numpy para gerar um intervalo de coordenadas e assim classificar o cliente.

    :param float latitude: Latitude do cliente.
    :param float longitude: Longitude do cliente.
    :return: Classificação do cliente conforme parâmetros do arquivo CLIENT_CLASSIFICATION.
    :rtype: str
    """
    classification = ""
    if (
        latitude in CLIENT_CLASSIFICATION["especial"]["latitude"] and
        longitude in CLIENT_CLASSIFICATION["especial"]["longitude"]
            ):
        classification = "especial"
    elif (
            latitude in CLIENT_CLASSIFICATION["normal"]["latitude"] and
            longitude in CLIENT_CLASSIFICATION["normal"]["longitude"]
            ):
        classification = "normal"
    else:
        classification = "trabalhoso"
    return classification


def get_region_by_state(state: str) -> str:
    """
    Informa a qual região o cliente pertence a partir do seu estado. O estado pode\
    conter acentos ortográficos.

    :param str state: Estado do cliente.
    :return: Região do cliente.
    :rtype: str
    """
    state_striped_accents = strip_accents(state)
    return ESTADOS_REGIOES.get(state_striped_accents)


def contact_to_e164(contact_number: str) -> str:
    """
    Transforma um número de telefone o celular no padrão E.164. O número pode conter\
    caracteres não númericos, i.e, (51) 12345-6655.

    :param str contact_number: Número de telefone ou celular.
    :return: Número no padrão E.164.
    :rtype: str
    """
    contact_only_numbers = re.sub(RE_ONLY_NUMBERS, "", contact_number)
    return "+55" + contact_only_numbers


def client_etl():
    """
    Rotina principal para carga da base de dados. Podem ser fornecidos arquivos\
    csv ou json. A rotina é executada em um container diferente da API, a partir \
    dos logs do container em que a rotina principal é executada é possível verificar\
    seu status e se encontra pronta (READY).

    Duas coleções são criadas input contendo os dados do cliente antes da manipulação \
    e output dados do cliente depois da manipulação.

    :raises NotImplementedError: Caso um arquivo diferente de csv ou json seja fornecido.
    """
    logger.log("API STATUS", "[-] API NOT READY")
    try:
        if "json" in CLIENT_INPUT_URL:
            clients_request = requests.get(url=CLIENT_INPUT_URL)
            if clients_request.status_code != 200:
                logger.error("CLIENT INPUT ERROR", "[-] ERRO AO EFETUAR REQUEST")
                raise ServiceException(clients_request.status_code, clients_request.word)
            clients = clients_request.json()["results"]
        elif "csv" in CLIENT_INPUT_URL:
            clients = csv_to_dict(CLIENT_INPUT_URL)["results"]
        else:
            raise NotImplementedError("O tipo de arquivo não é suportado pela aplicação")
        qtd_clients, current_record = len(clients), 1
        for client in clients:
            logger.log("API STATUS", f"[+] EXECUTANDO CLIENTE {current_record} DE {qtd_clients}")
            object_id_input = insert(client, collection="input")
            latitude, longitude = map(float, client["location"]["coordinates"].values())
            client["client_type"] = classify_client(latitude, longitude)
            client["location"]["region"] = get_region_by_state(client["location"]["state"])
            client["mobile_numbers"] = [contact_to_e164(client["cell"])]
            del client["cell"]
            client["telephone_numbers"] = [contact_to_e164(client["phone"])]
            del client["phone"]
            client["nationality"] = "BR"
            client["gender"] = "f" if client["gender"].lower() == "female" else "m"
            client["birthday"] = client["dob"]["date"]
            del client["dob"]
            client["registered"] = client["registered"]["date"]
            client["object_id_input"] = object_id_input
            insert(client, collection="output")
            current_record += 1
        logger.log("API STATUS", "[+] API READY")

    except requests.exceptions.ConnectionError as connection_error:
        logger.error("CLIENT INPUT ERROR", "[-] ERRO AO EFETUAR REQUEST")
        raise ServiceException(500, connection_error)


if __name__ == "__main__":
    client_etl()
