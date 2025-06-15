from sqlalchemy.orm import Session
from models.m_interaccion import Interaccion


def crearInteracion(db: Session, usuario_id: int, noticia_id: int):
    db_interaccion = Interaccion(
        usuario_id=usuario_id,
        noticia_id=noticia_id
    )
    db.add(db_interaccion)
    db.commit()
    db.refresh(db_interaccion)
    return db_interaccion
