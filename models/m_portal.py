from sqlalchemy import Column, Integer, String
from database import Base


class PortalNoticia(Base):
    __tablename__ = "portales_noticia"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    logo = Column(String(100))
    url_base = Column(String(255), nullable=False)
