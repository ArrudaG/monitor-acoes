import os
import requests

TOKEN = os.getenv("TOKEN")

def preco_acao(ticker):
    try:
        url = f"https://brapi.dev/api/quote/{ticker}?token={TOKEN}"
        r = requests.get(url, timeout=10)
        data = r.json()
        return data["results"][0]["regularMarketPrice"]
    except Exception as e:
        print(f"Erro ao buscar preço de {ticker}: {e}")
        return None
