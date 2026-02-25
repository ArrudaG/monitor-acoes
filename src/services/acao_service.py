import logging

import requests

from src.config.settings import ACAO_API_KEY

def buscar_preco(ticker):
    try:
        url = f"https://brapi.dev/api/quote/{ticker}?token={ACAO_API_KEY}"
        r = requests.get(url, timeout=10)

        r.raise_for_status()

        data = r.json()
        return data["results"][0]["regularMarketPrice"]

    except requests.Timeout as error:
        logging.error(f"O tempo máximo para buscar {ticker} foi atingido: {error}")
        return None

    except requests.RequestException as error:
        logging.error(f"Erro HTTP ao buscar preço de {ticker}: {error}")
        return None

    except (KeyError, IndexError) as error:
        logging.error(f"Estrutura inesperada da resposta para {ticker}: {error}")
        return None