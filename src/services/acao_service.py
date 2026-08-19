import logging
import requests
from sqlalchemy import update
from src.services.database_service import engine
from src.models.ticker_model import Ticker
from src.services.brapi_api_service import buscar_cotacoes
from src.config.settings import BRAPI_API_KEY
from src.services.notificacao_service import NotificacaoService

class AcaoService:
    @staticmethod
    def buscar_preco(ticker):
        """
        Busca o preço da ação usando a API brapi.dev
        """
        try:
            url = f"https://brapi.dev/api/quote/{ticker}?token={BRAPI_API_KEY}"
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            data = r.json()

            results = data.get("results")
            if not results:
                logging.error(f"Nenhum resultado encontrado para {ticker}")
                return None

            preco = results[0].get("regularMarketPrice")
            if preco is None:
                logging.error(f"Nenhum preco encontrado para {ticker}")
                return None

            return preco

        except requests.Timeout as error:
            logging.error(f"O tempo máximo para buscar {ticker} foi atingido: {error}")
            return None

        except requests.RequestException as error:
            logging.error(f"Erro HTTP ao buscar preço de {ticker}: {error}")
            return None

    @staticmethod
    def alterar_valor_ticker():
        tickers = NotificacaoService.obter_tickers()
        resultado = buscar_cotacoes(tickers)

        with engine() as session:
            for ticker in resultado:
                preco = ticker.get("regularMarketPrice")
                porcentagem = ticker.get("regularMarketChangePercent")

                if preco is not None and porcentagem is not None:
                        stmt = (
                            update(Ticker)
                            .where(Ticker.ticker == ticker.get("symbol"))
                            .values(
                                valor_atual=preco,
                                valor_porcentagem=porcentagem
                            ))
                        session.execute(stmt)

        session.commit()
        return None

    @staticmethod
    def buscar_diario(ticker):
        symbols = ",".join(ticker)
        url = f"https://brapi.dev/api/quote/{symbols}?token={BRAPI_API_KEY}"

        reponse = requests.get(url, timeout=100)
        data = reponse.json()

        valor_atual = []
        valor_variacao = []
        ticker = []
        for ativo in data.get("results", []):
            ticker.append(ativo.get("symbol"))
            valor_atual.append(ativo.get("regularMarketPrice"))
            valor_variacao.append(ativo.get("regularMarketChangePercent"))
        return ticker, valor_atual, valor_variacao