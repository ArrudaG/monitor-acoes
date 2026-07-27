import os
from dotenv import load_dotenv

load_dotenv()

ACAO_API_KEY = os.getenv('ACAO_API_KEY')
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_TO = os.getenv("EMAIL_TO")