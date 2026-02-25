import smtplib
import logging

from email.mime.text import MIMEText
from src.config.settings import EMAIL_USER, EMAIL_PASSWORD, EMAIL_TO

class EmailService:

    def __init__(self):

        if not EMAIL_USER or not EMAIL_PASSWORD:
            raise ValueError("Credenciais de email não carregadas")

        if not EMAIL_TO:
            raise ValueError("Email do destinatário não carregado")

        self.user = EMAIL_USER
        self.password = EMAIL_PASSWORD
        self.to = EMAIL_TO

    def enviar(self, assunto, mensagem):

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
            logging.info("Email enviado com sucesso")

        except Exception as error:
            logging.error(f"Erro ao enviar o email: {error}")
            raise