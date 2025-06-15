from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, DATETIME
from database import Base


class Interaccion(Base):
    __tablename__ = "interaccion_noticia_usuario"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    noticia_id = Column(Integer, ForeignKey("noticia.id"), nullable=False)
    fecha_leido = Column(DATETIME, default=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
    utilidad = Column(Integer, nullable=True)  # Valoración de utilidad de la noticia
    resumen_claro = Column(Integer, nullable=True)  # Valoración de claridad del resumen

