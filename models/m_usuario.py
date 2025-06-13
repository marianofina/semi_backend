from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from .m_preferencia import Preferencia
from database import Base


class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    fecha_nac = Column(Date, nullable=False)
    preferencias = relationship("Preferencia", back_populates="usuario", cascade="all, delete-orphan")

