import logging
import smtplib
from email.mime.text import MIMEText
from src.config.settings import EMAIL_USER, EMAIL_PASSWORD, EMAIL_TO

class EmailService:
    def __init__(self):
        """
        Inicializa o serviço de email com as credenciais e destinatário configurados.
        """
        if not EMAIL_USER or not EMAIL_PASSWORD:
            raise ValueError("Credenciais de email não carregadas")
        if not EMAIL_TO:
            raise ValueError("Email do destinatário não carregado")

        self.user = EMAIL_USER
        self.password = EMAIL_PASSWORD
        self.to = EMAIL_TO

    def enviar(self, assunto, mensagem):
        """
        Envia um email com o assunto e mensagem fornecidos.
        """
        try:
            msg = MIMEText(mensagem)
            msg["Subject"] = assunto
            msg["From"] = self.user
            msg["To"] = self.to

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(self.user, self.password)
                server.sendmail(
                    self.user,
                    self.to,
                    msg.as_string()
                )
            return "Email enviado com sucesso"

        except smtplib.SMTPException as error:
            logging.error(f"Erro ao enviar o email: {error}")
            raise Exception(f"Erro ao enviar o email: {error}")