from database import Base
from sqlalchemy import Column, Integer, ForeignKey, Boolean


class PortalBloqueado(Base):
    __tablename__ = "portales_bloq"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    portal_id = Column(Integer, ForeignKey("portales_noticia.id"), nullable=False)
    bloq = Column(Boolean, nullable=False, default=True)
