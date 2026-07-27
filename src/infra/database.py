from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import os

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("A variável DATABASE_URL não está definida no arquivo .env!")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

#Teste para conexão com o db
def inicializar_banco():
    try:
        with engine.connect() as conexao:
            conexao.execute(text("SELECT 1"))
    except SQLAlchemyError as e:
        raise RuntimeError(f"Erro ao tentar se conectar com o banco de dados: {e}") from e