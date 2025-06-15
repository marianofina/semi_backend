from sqlalchemy.orm import Session
from models.m_noticia import Noticia
from schemas.s_noticia import NoticiaCreate
from crud.c_preferencia import listar_preferencias
from crud.c_port_bloq import obtener_portales_bloq


def crear_noticia(db: Session, noticia: NoticiaCreate):
    db_noticia = Noticia(
        titulo=noticia.titulo,
        contenido=noticia.contenido,
        resumen=noticia.resumen,
        portal_id=noticia.portal_id,
        tematica_id=noticia.tematica_id,
        autor=noticia.autor
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
    preferencias = listar_preferencias(db, user_id) or []
    tematicas = [p.tematica_id for p in preferencias]

    portales_bloqueados = obtener_portales_bloq(db, user_id) or []
    portales_bloq_ids = [pb.portal_id for pb in portales_bloqueados]

    query = db.query(Noticia)

    if tematicas:
        query = query.filter(Noticia.tematica_id.in_(tematicas))
    if portales_bloq_ids:
        query = query.filter(Noticia.portal_id.notin_(portales_bloq_ids))

    query = query.filter(Noticia.resumen.isnot(None))

    return query.all()

