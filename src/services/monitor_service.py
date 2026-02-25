# import logging#

# from infra.logging_config import setup_logger#
# from infra.powershell_monitor import powershell_monitor#

# setup_logger()#
# powershell_monitor()#


# logging.info("Monitor iniciado")#

class MonitorService():
    def __init__(self, acao_service, email_service, estado_service):
        self.acao_service = acao_service
        self.email_service = email_service
        self.estado_service = estado_service

    def executar(self, ativos, upper_limits, lower_limits):

        alertas = self.estado_service.carregar_estado()

        for ativo in ativos:
            alertas.setdefault(f"LOWER_{ativo}", False)
            alertas.setdefault(f"UPPER_{ativo}", False)

        for i, ativo in enumerate(ativos):

            preco = self.acao_service(ativo)

            print(f"{ativo}: {preco}")

            if lower_limits:
                lower = lower_limits[i]
                estado_lower = f"LOWER_{ativo}"

                if preco <= lower:
                    if not alertas.get(estado_lower, False):
                        self.email_service.enviar(f"{ativo} abaixo de {lower}", f"Preço: {preco}\n")
                        alertas[estado_lower] = True
                else:
                    alertas[estado_lower] = False

            if upper_limits:
                upper = upper_limits[i]
                estado_upper = f"UPPER_{ativo}"

                if preco >= upper:
                    if not alertas.get(estado_upper, False):
                        self.email_service.enviar(f"{ativo} acima de {upper}", f"Preço: {preco}\n")
                        alertas[estado_upper] = True
                else:
                    alertas[estado_upper] = False

        self.estado_service.salvar_estado(alertas)