from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship


class TematicaNoticia(Base):
    __tablename__ = "tematica_noticias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)

    noticia = relationship("Noticia", back_populates="tematica")
