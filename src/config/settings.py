import os
from dotenv import load_dotenv

load_dotenv()

BRAPI_API_KEY = os.getenv('ACAO_API_KEY')
DATABASE_URI = os.getenv('DATABASE_URI')
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_TO = os.getenv("EMAIL_TO")