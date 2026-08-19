import requests
from src.config.settings import BRAPI_API_KEY


def buscar_cotacoes(tickers: list[str]) -> list[dict]:
    symbols = ",".join(tickers)
    url = f"https://brapi.dev/api/quote/{symbols}?token={BRAPI_API_KEY}"

    response = requests.get(url)
    response.raise_for_status()

    dados = response.json()
    return dados.get("results", [])