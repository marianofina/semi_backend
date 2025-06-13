from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base


class Preferencia(Base):
    __tablename__ = "preferencia_noticias_usuario"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    tematica_id = Column(Integer, ForeignKey("tematica_noticias.id"))
    interesa = Column(Boolean, nullable=False)
    usuario = relationship("Usuario", back_populates="preferencias")
