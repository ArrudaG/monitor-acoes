from src.services.acao_service import AcaoService
from src.services.email_service import EmailService
from src.services.notificacao_service import NotificacaoService

def main():

    monitor = NotificacaoService(AcaoService(), EmailService())

    monitor.retornar_pendentes()

if __name__ == "__main__":
    main()