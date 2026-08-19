

from sqlalchemy import select

from src.models.ticker_model import Ticker
from src.infra.database import SessionLocal
from src.models.notificacao_model import Notificacao

class NotificacaoService:
    def __init__(self, acao_service, email_service):
        self.acao_service = acao_service
        self.email_service = email_service

    @staticmethod
    def obter_tickers() -> list[str]:
        with SessionLocal() as session:
            stmt = (
                select(Ticker.ticker)
            )
            resultados = session.scalars(stmt).all()

            return resultados

    @staticmethod
    def listar_pendentes():
        with SessionLocal() as session:
            stmt = (
                select(
                    Notificacao.id,
                    Notificacao.user_id,
                    Notificacao.simbolo_ativo,
                    Notificacao.tipo_gatilho,
                    Notificacao.valor_alvo,
                )
                .where(Notificacao.ja_notificou.is_(False))
            )

            return session.execute(stmt).all()

    @staticmethod
    def marcar_como_notificada(id_notificacao):
        with SessionLocal() as session:
            notificacao = session.get(Notificacao, id_notificacao)

            if notificacao is None:
                return
            notificacao.ja_notificou = True
            session.commit()

    def retornar_pendentes(self):
        precos = {}
        for ticker in self.obter_tickers():
            preco = self.acao_service.buscar_preco(ticker)
            if preco is not None:
                precos[ticker] = preco

        notificacoes = self.listar_pendentes()

        for notificacao in notificacoes:
            simbolo_ativo = notificacao.simbolo_ativo
            if simbolo_ativo not in precos:
                continue

            preco = precos[notificacao.simbolo_ativo]

            if notificacao.tipo_gatilho == "ABOVE" and preco >= notificacao.valor_alvo:
                try:
                    self.email_service.enviar(f"{notificacao.simbolo_ativo} acima de R$ {notificacao.valor_alvo}", f"Preço: R${preco}")
                    self.marcar_como_notificada(notificacao.id)
                except Exception as e:
                    print(f"Erro ao enviar email: {e}")
            elif notificacao.tipo_gatilho == "BELOW" and preco <=notificacao.valor_alvo:
                try:
                    self.email_service.enviar(f"{notificacao.simbolo_ativo} abaixo de R$ {notificacao.valor_alvo}", f"Preço: R${preco}")
                    self.marcar_como_notificada(notificacao.id)
                except Exception as e:
                    print(f"Erro ao enviar email: {e}")