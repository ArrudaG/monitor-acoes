import os
from dotenv import load_dotenv

load_dotenv()

ACAO_API_KEY = os.getenv('ACAO_API_KEY')
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_TO = os.getenv("EMAIL_TO")

PAR_MONITORADO = [
  "PETR4", "ITSA3", "BBDC3", "ABEV3", "TOTS3", "MELI34"
]

ACAO_LOWER_LIMIT = [35.00, 12.72, 16.87, 14.74, 36.00, 70]

ACAO_UPPER_LIMIT = []
