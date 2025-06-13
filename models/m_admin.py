from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base


class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
