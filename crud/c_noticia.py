from sqlalchemy.orm import Session
from models.m_noticia import Noticia
from schemas.s_noticia import NoticiaCreate
from crud.c_preferencia import listar_preferencias


def crear_noticia(db: Session, noticia: NoticiaCreate):
    db_noticia = Noticia(
        titulo=noticia.titulo,
        contenido=noticia.contenido,
        resumen=noticia.resumen,
        portal_id=noticia.portal_id,
        tematica_id=noticia.tematica_id,
        autor_id=noticia.autor_id
    )
    db.add(db_noticia)
    db.commit()
    db.refresh(db_noticia)
    return db_noticia


def obtener_noticias(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Noticia).order_by(Noticia.id).offset(skip).limit(limit).all()


def obtener_noticia(db: Session, noticia_id: int):
    return db.query(Noticia).filter(Noticia.id == noticia_id).first()


def obtener_noticias_por_usuario(db: Session, user_id: int):
    preferencias = listar_preferencias(db, user_id)  # lista de Preferencia
    tematicas = [p.tematica_id for p in preferencias]  # extraemos solo los IDs de tematica

    if not tematicas:
        return []  # si no tiene preferencias, no traemos nada

    return db.query(Noticia).filter(Noticia.tematica_id.in_(tematicas), Noticia.resumen.isnot(None)).all()
