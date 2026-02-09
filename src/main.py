import time
import logging

from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

load_dotenv()

from infra.estado import carregar_estado, salvar_estado
#from infra.logging_config import setup_logger#
from services.email_service import enviar_email
from services.acao_service import preco_acao
from config.settings import *
#from infra.powershell_monitor import powershell_monitor#

#setup_logger()#
#powershell_monitor()#

alertas = carregar_estado()

#logging.info("Monitor iniciado")#

while True:
    acao0 = preco_acao(PAR_MONITORADO[0])
    acao1 = preco_acao(PAR_MONITORADO[1])
    acao2 = preco_acao(PAR_MONITORADO[2])
    acao3 = preco_acao(PAR_MONITORADO[3])

    if acao0 is not None:
        print(f"{PAR_MONITORADO[0]}: {acao0}")
      
        if acao0 < ACAO_LOWER_LIMIT0:
            if not alertas.get(LOWER_ALERT_KEY0, False):
                enviar_email(f"{PAR_MONITORADO[0]} abaixo de {ACAO_LOWER_LIMIT0}",f"Preço: {acao0}\n")
                alertas[LOWER_ALERT_KEY0] = True
            
        else:
            alertas[LOWER_ALERT_KEY0] = False

    if acao1 is not None:
        print(f"{PAR_MONITORADO[1]}: {acao1}")
      
        if acao1 < ACAO_LOWER_LIMIT1:
            if not alertas.get(LOWER_ALERT_KEY1, False):
                enviar_email(f"{PAR_MONITORADO[1]} abaixo de {ACAO_LOWER_LIMIT1}",
                         f"Preço: {acao1}\n")
                alertas[LOWER_ALERT_KEY1] = True
            
        else:
            alertas[LOWER_ALERT_KEY1] = False

    if acao2 is not None:
        print(f"{PAR_MONITORADO[2]}: {acao2}")
      
        if acao2 < ACAO_LOWER_LIMIT2:
            if not alertas.get(LOWER_ALERT_KEY2, False):
                enviar_email(f"{PAR_MONITORADO[2]} abaixo de {ACAO_LOWER_LIMIT2}",
                         f"Preço: {acao2}\n")
                alertas[LOWER_ALERT_KEY2] = True
            
        else:
            alertas[LOWER_ALERT_KEY2] = False

    if acao3 is not None:
        print(f"{PAR_MONITORADO[3]}: {acao3}\n")
      
        if acao3 < ACAO_LOWER_LIMIT3:
            if not alertas.get(LOWER_ALERT_KEY3, False):
                enviar_email(f"{PAR_MONITORADO[3]} abaixo de {ACAO_LOWER_LIMIT3}",
                         f"Preço: {acao3}\n")
                alertas[LOWER_ALERT_KEY3] = True
            
        else:
            alertas[LOWER_ALERT_KEY3] = False
          
    salvar_estado(alertas)
