from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from src.config.settings import DATABASE_URI


def testar_conexao():
    if not DATABASE_URI:
        print("❌ ERRO: A variável DATABASE_URL não foi definida no arquivo .env!")
        return

    print("🔄 Conectando ao PostgreSQL...")

    try:
        engine = create_engine(DATABASE_URI)

        with engine.connect() as conexao:
            resultado = conexao.execute(text("SELECT version();"))
            versao_db = resultado.scalar()

            print("✅ Conexão realizada com sucesso!\n")
            print(f"📊 Informações do Banco:\n{versao_db}")

    except SQLAlchemyError as e:
        print("\n❌ Falha ao conectar no banco de dados!")
        print(f"Detalhes do erro:\n{e}")
    except Exception as e:
        print(f"\n❌ Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    testar_conexao()