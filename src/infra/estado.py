import json
import os

from src.config.settings import LOWER_ALERT_KEY0, LOWER_ALERT_KEY1, LOWER_ALERT_KEY2, LOWER_ALERT_KEY3

ESTADO_FILE = "estado.json"

def carregar_estado():
    if os.path.exists(ESTADO_FILE):
        with open(ESTADO_FILE, "r") as f:
            return json.load(f)
    else:
        estado = {}

    estado.setdefault(LOWER_ALERT_KEY0, False)
    estado.setdefault(LOWER_ALERT_KEY1, False)
    estado.setdefault(LOWER_ALERT_KEY2, False)
    estado.setdefault(LOWER_ALERT_KEY3, False)

    return estado


def salvar_estado(alertas):
    with open(ESTADO_FILE, "w") as f:
        json.dump(alertas, f, indent=2)
