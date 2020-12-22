import re
import unicodedata

import requests
from loguru import logger

from cadastro_clientes.modules.client import insert
from cadastro_clientes.exceptions.service import ServiceException
from cadastro_clientes.config import (
    CLIENT_INPUT_JSON, CLIENT_CLASSIFICATION, ESTADOS_REGIOES, RE_ONLY_NUMBERS
    )


def csv_to_dict(url: str) -> dict:
    pass


def strip_accents(word: str) -> str:
    try:
        word = unicode(word, "utf-8")
    except (TypeError, NameError):
        pass
    word = unicodedata.normalize("NFD", word)
    word = word.encode("ascii", "ignore")
    word = word.decode("utf-8")
    return str(word).lower()


def classify_client(latitude: float, longitude: float) -> str:
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
    state_striped_accents = strip_accents(state)
    return ESTADOS_REGIOES.get(state_striped_accents)


def contact_to_e164(contact_number: str) -> str:
    contact_only_numbers = re.sub(RE_ONLY_NUMBERS, "", contact_number)
    return "+55" + contact_only_numbers


def client_etl():
    logger.log("API STATUS", "[-] API NOT READY")
    try:
        clients_request = requests.get(url=CLIENT_INPUT_JSON)
        if clients_request.status_code != 200:
            logger.error("CLIENT INPUT ERROR", "[-] ERRO AO EFETUAR REQUEST")
            raise ServiceException(clients_request.status_code, clients_request.word)

        clients = clients_request.json()["results"]
        logger.log("CLIENT INPUT ALERT", f"[+] INÍCIO DO TRATAMENTO DOS DADOS DE ENTRADA")
        for client in clients:
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
        logger.log("API STATUS", "[+] API READY")

    except requests.exceptions.ConnectionError as connection_error:
        logger.error("CLIENT INPUT ERROR", "[-] ERRO AO EFETUAR REQUEST")
        raise ServiceException(500, connection_error)


if __name__ == "__main__":
    client_etl()
