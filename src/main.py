import time
import logging

from dotenv import load_dotenv

from infra.estado import carregar_estado, salvar_estado
from services.email_service import enviar_email
from services.acao_service import preco_acao
from config.settings import *

load_dotenv()
powershell_monitor()

alertas = carregar_estado()

  while True:
    acao0 = preco_acao(PAR_MONITORADO0)
    acao1 = preco_acao(PAR_MONITORADO1)
    acao2 = preco_acao(PAR_MONITORADO2)
    acao3 = preco_acao(PAR_MONITORADO3)
    
    if acao0:
        print(f"{PAR_MONITORADO0}: {acao0}")
      
        if acao0 < ACAO_LOWER_LIMIT0:
          if not alertas[LOWER_ALERT_KEY0]:
            enviar_email(f"{PAR_MONITORADO0} abaixo de {ACAO_LOWER_LIMIT0}",
                         f"Preço: {ACAO_LOWER_LIMIT0}\n")
            alertas["LOWER_ALERT_KEY0"] = True
            
        else:
            alertas["LOWER_ALERT_KEY0"] = False

    if acao1:
        print(f"{PAR_MONITORADO1}: {acao1}")
      
        if acao1 < ACAO_LOWER_LIMIT1:
          if not alertas[LOWER_ALERT_KEY1]:
            enviar_email(f"{PAR_MONITORADO1} abaixo de {ACAO_LOWER_LIMIT1}",
                         f"Preço: {ACAO_LOWER_LIMIT1}\n")
            alertas["LOWER_ALERT_KEY1"] = True
            
        else:
            alertas["LOWER_ALERT_KEY1"] = False

    if acao2:
        print(f"{PAR_MONITORADO2}: {acao2}")
      
        if acao2 < ACAO_LOWER_LIMIT2:
          if not alertas[LOWER_ALERT_KEY2]:
            enviar_email(f"{PAR_MONITORADO2} abaixo de {ACAO_LOWER_LIMIT2}",
                         f"Preço: {ACAO_LOWER_LIMIT2}\n")
            alertas["LOWER_ALERT_KEY2"] = True
            
        else:
            alertas["LOWER_ALERT_KEY2"] = False

    if acao3:
        print(f"{PAR_MONITORADO3}: {acao3}")
      
        if acao3 < ACAO_LOWER_LIMIT3:
          if not alertas[LOWER_ALERT_KEY3]:
            enviar_email(f"{PAR_MONITORADO3} abaixo de {ACAO_LOWER_LIMIT3}",
                         f"Preço: {ACAO_LOWER_LIMIT3}\n")
            alertas["LOWER_ALERT_KEY3"] = True
            
        else:
            alertas["LOWER_ALERT_KEY3"] = False
          
salvar_estado(alertas)

if __name__ == "__main__":
    monitor()
