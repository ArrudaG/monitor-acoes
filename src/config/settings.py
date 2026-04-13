import os
from dotenv import load_dotenv

load_dotenv()

ACAO_API_KEY = os.getenv('ACAO_API_KEY')
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_TO = os.getenv("EMAIL_TO")

PAR_MONITORADO = [
  "PETR4", "ITSA3", "BBDC4", "ABEV3", "TOTS3", "MGLU3", "BBSE3", "TAEE4", "VALE3"
]

ACAO_LOWER_LIMIT = [36.00, 13.50, 18.00, 14.74, 33.00, 8.00, 33.60, 13.9, 74.9]

ACAO_UPPER_LIMIT = [100, 15.00, 21, 16.2, 37.00, 9.85, 38.00, 100, 100]
