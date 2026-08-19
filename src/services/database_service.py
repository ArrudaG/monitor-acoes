from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from src.infra.database import SessionLocal, Base, engine

def atualizar_banco():
    try:
        from src.models.ticker_model import Ticker

        Base.metadata.create_all(bind=engine)

        with SessionLocal.connect() as conexao:
            conexao.execute(text("SELECT 1"))
            print("Tabela criada/verificada com sucesso!")

    except SQLAlchemyError as e:
        raise RuntimeError(f"Erro ao tentar se conectar com o banco de dados: {e}") from e
    except ValueError as e:
        raise RuntimeError(f"Erro de configuração: {e}") from e

if __name__ == "__main__":
    atualizar_banco()