from sqlalchemy import select
from infra.database import SessionLocal
from models.notificacao_model import Notificacao

class NotificacaoService():
    def __init__(self, acao_service, email_service):
        self.acao_service = acao_service
        self.email_service = email_service

    def obter_tickers_unicos_para_pesquisa(self) -> set[str]:
        with SessionLocal() as session:
            stmt = (
                select(Notificacao.simbolo_ativo)
                .where(Notificacao.ja_notificou.is_(False))
                .distinct()
            )

            resultados = session.scalars(stmt).all()

            return set(resultados)

    def listar_pendentes(self):
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

    def retornar_pendentes(self):
        precos = {}
        for ticker in self.obter_tickers_unicos_para_pesquisa():
            precos[ticker] = self.acao_service.buscar_preco(ticker)

        notificacoes = self.listar_pendentes()

        for notificacao in notificacoes:
            preco = precos[notificacao.simbolo_ativo]

            if preco is None:
                continue

            if notificacao.tipo_gatilho == "ABOVE" and preco >= notificacao.valor_alvo:
                enviado = self.email_service.enviar(f"{notificacao.simbolo_ativo} acima de R$ {notificacao.valor_alvo}", f"Preço: R${preco}")
                if enviado:
                    self.marcar_como_notificada(notificacao.id)
            elif notificacao.tipo_gatilho == "BELOW" and preco <=notificacao.valor_alvo:
                enviado = self.email_service.enviar(f"{notificacao.simbolo_ativo} abaixo de R$ {notificacao.valor_alvo}", f"Preço: R${preco}")
                if enviado:
                    self.marcar_como_notificada(notificacao.id)

    def marcar_como_notificada(self, id_notificacao):
        with SessionLocal() as session:
            notificacao = session.get(Notificacao, id_notificacao)

            if notificacao is None:
                return
            notificacao.ja_notificou = True

            session.commit()