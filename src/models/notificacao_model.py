from sqlalchemy import String, Boolean, Integer, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Notificacao(Base):
    __tablename__ = "Notificacoes"

    id: Mapped[int] = mapped_column("Id", Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column("UserId", Integer)
    simbolo_ativo: Mapped[str] = mapped_column("SimboloAtivo", String)
    tipo_gatilho: Mapped[str] = mapped_column("TipoGatilho", String)
    valor_alvo: Mapped[float] = mapped_column("ValorAlvo", Float)
    ja_notificou: Mapped[bool] = mapped_column("JaNotificou", Boolean)