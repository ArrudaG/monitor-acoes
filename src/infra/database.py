from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm.session import sessionmaker
from src.config.settings import DATABASE_URI

if not DATABASE_URI:
    raise ValueError("DATABASE_URI não configurada. Verifique o arquivo .env na raiz do projeto.")
engine = create_engine(DATABASE_URI)

SessionLocal = sessionmaker(bind=engine)
class Base(DeclarativeBase):
    pass
