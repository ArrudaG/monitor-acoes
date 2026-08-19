from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm.session import sessionmaker

from src.config.settings import DATABASE_URI

engine = create_engine(DATABASE_URI)

SessionLocal = sessionmaker(bind=engine)
class Base(DeclarativeBase):
    pass