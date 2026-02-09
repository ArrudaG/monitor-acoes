import json
import os

from src.config.settings import LOWER_ALERT_KEY, UPPER_ALERT_KEY

ESTADO_FILE = "estado.json"

def carregar_estado():
    if os.path.exists(ESTADO_FILE):
        with open(ESTADO_FILE, "r") as f:
            return json.load(f)
    else:
        estado = {}

    estado.setdefault(LOWER_ALERT_KEY, False)
    estado.setdefault(UPPER_ALERT_KEY, False)

    return estado


def salvar_estado(alertas):
    with open(ESTADO_FILE, "w") as f:
        json.dump(alertas, f, indent=2)
