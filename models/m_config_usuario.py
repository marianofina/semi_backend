from sqlalchemy import Column, Integer, ForeignKey, Float
from database import Base


class ConfigUsuario(Base):
    __tablename__ = "config_usuarios"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    notificaciones_activadas = Column(Integer, default=1)  # 1 para activadas, 0 para desactivadas
    nivel_resumen = Column(Float, default=0.5)
