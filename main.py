from src.services.monitor_service import MonitorService
from src.services.email_service import EmailService
from src.services.acao_service import buscar_preco
from src.infra.estado_service import EstadoService
from src.config.settings import ACAO_UPPER_LIMIT, ACAO_LOWER_LIMIT, PAR_MONITORADO

def main():

    monitor = MonitorService(
        acao_service=buscar_preco,
        email_service=EmailService(),
        estado_service=EstadoService()
    )

    monitor.executar(PAR_MONITORADO, ACAO_UPPER_LIMIT, ACAO_LOWER_LIMIT)

if __name__ == "__main__":
    main()