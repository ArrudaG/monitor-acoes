import os
import smtplib
import logging

from email.mime.text import MIMEText

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_TO = os.getenv("EMAIL_TO")

def enviar_email(assunto, mensagem):
    if not EMAIL_USER or not EMAIL_PASSWORD or not EMAIL_TO:
        raise ValueError("Credenciais de email não carregadas")

    try:
        msg = MIMEText(mensagem)
        msg["Subject"] = assunto
        msg["From"] = EMAIL_USER
        msg["To"] = EMAIL_TO

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.sendmail(
                EMAIL_USER,
                EMAIL_TO,
                msg.as_string()
            )
        logging.info("Email enviado com sucesso")

    except Exception as e:
        print("ERRO SMTP:", e)
        logging.error(f"Erro ao enviar o email: {e}")
