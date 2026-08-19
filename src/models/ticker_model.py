from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column
from src.infra.database import Base

class Ticker(Base):
    __tablename__ = "Tickers"

    id: Mapped[int] = mapped_column("Id", Integer, primary_key=True)
    ticker: Mapped[str] = mapped_column("Ticker", String)
    valor_atual: Mapped[float] = mapped_column("ValorAtual", Float)
    valor_porcentagem: Mapped[float] = mapped_column("ValorPorcentagem", Float)