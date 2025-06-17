from sqlalchemy.orm import Session
from models.m_interaccion import Interaccion


def crearInteracion(db: Session, usuario_id: int, noticia_id: int):
    inte = obtener_interaccion(db, usuario_id, noticia_id)
    if not inte:
        inte = Interaccion(
            usuario_id=usuario_id,
            noticia_id=noticia_id
        )
        db.add(inte)
        db.commit()
        db.refresh(inte)
    return inte


def obtener_interaccion(db: Session, usuario_id: int, noticia_id: int):
    return db.query(Interaccion).filter(
        Interaccion.usuario_id == usuario_id,
        Interaccion.noticia_id == noticia_id
    ).first()


def update_utilidad(db: Session, usuario_id: int, noticia_id: int, utilidad: int):
    inte = obtener_interaccion(db, usuario_id, noticia_id)
    if inte:
        inte.utilidad = utilidad
        db.commit()
        db.refresh(inte)
    return inte


def update_resumen_claro(db: Session, usuario_id: int, noticia_id: int, resumen_claro: int):
    inte = obtener_interaccion(db, usuario_id, noticia_id)
    if inte:
        inte.resumen_claro = resumen_claro
        db.commit()
        db.refresh(inte)
    return inte
