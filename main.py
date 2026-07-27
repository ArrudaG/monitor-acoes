from services.acao_service import AcaoService
from services.email_service import EmailService
from services.notificacao_service import NotificacaoService

def main():

    monitor = NotificacaoService(AcaoService(), EmailService())

    monitor.retornar_pendentes()

if __name__ == "__main__":
    main()