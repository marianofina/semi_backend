from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from datetime import datetime
from database import Base


class Noticia(Base):
    __tablename__ = "noticia"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    contenido = Column(Text, nullable=False)
    resumen = Column(Text)
    fecha_publicacion = Column(DateTime, default=datetime.utcnow)
    portal_id = Column(Integer, ForeignKey("portales_noticia.id"))
    tematica_id = Column(Integer, ForeignKey("tematica_noticias.id"))
    autor_id = Column(String(100))
