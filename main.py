from src.services.acao_service import AcaoService
from src.services.email_service import EmailService
from src.services.notificacao_service import NotificacaoService

def main():
    acao_service = AcaoService()
    email_service = EmailService()
    monitor = NotificacaoService(acao_service, email_service)
    acao_service.alterar_valor_ticker()
    monitor.retornar_pendentes()

if __name__ == "__main__":
    main()
