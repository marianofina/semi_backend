from sqlalchemy.orm import Session
from models.m_config_usuario import ConfigUsuario


def crearConfigUsuario(db: Session, usuario_id: int, notificaciones_activadas, nivel_resumen):
    config = obtener_config_usuario(db, usuario_id)

    if not config:
        # Crear nuevo
        config = ConfigUsuario(
            usuario_id=usuario_id,
            notificaciones_activadas=notificaciones_activadas,
            nivel_resumen=nivel_resumen
        )
        db.add(config)
    else:
        # Actualizar existente
        config.notificaciones_activadas = notificaciones_activadas
        config.nivel_resumen = nivel_resumen

    db.commit()
    db.refresh(config)
    return config



def obtener_config_usuario(db: Session, usuario_id: int):
    return db.query(ConfigUsuario).filter(ConfigUsuario.usuario_id == usuario_id).first()
