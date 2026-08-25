from src.services.email_service import EmailService


def test_enviar_email_funcionamento():
    email_service = EmailService()
    email_service.to = "gabrielarr1227@gmail.com"
    assunto = "Teste de Integração - Sistema de Notificação"
    mensagem = "Olá, Gabriel! Este é um email genérico de teste. Se você está lendo isso, significa que o seu EmailService foi configurado e está funcionando perfeitamente."
    resultado = email_service.enviar(assunto, mensagem)

    assert resultado == "Email enviado com sucesso"