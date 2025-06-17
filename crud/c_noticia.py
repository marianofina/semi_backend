from sqlalchemy.orm import Session
from models.m_noticia import Noticia
from schemas.s_noticia import NoticiaCreate
from crud.c_preferencia import listar_preferencias
from crud.c_port_bloq import obtener_portales_bloq
from sqlalchemy import text


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


def obtener_noticia(db: Session, usuario_id: int, noticia_id: int):
    r = db.execute(
        text("EXEC get_noticia_usuario @usuario_id = :usuario_id, @noticia_id = :noticia_id"),
        {"usuario_id": usuario_id, "noticia_id": noticia_id}
    ).first()
    resultado = {
            "id": r[0],
            "titulo": r[1],
            "resumen": r[2],
            "fecha_publicacion": r[3],
            "url_original": r[4],
            "portal_id": r[5],
            "portal_nombre": r[6],
            "tematica_id": r[7],
            "tematica_nombre": r[8],
            "autor": r[9],
            "interaccion_id": r[10],
            "fecha_leido": r[11],
            "utilidad": r[12],
            "resumen_claro": r[13]
        }

    return resultado


def obtener_noticias_por_usuario(db: Session, user_id: int):
    result = db.execute(
        text("EXEC obtener_noticias_usuario @usuario_id = :usuario_id"),
        {"usuario_id": user_id}
    ).fetchall()
    resultados = [
        {
            "id": r[0],
            "titulo": r[1],
            "resumen": r[2],
            "fecha_publicacion": r[3],
            "url_original": r[4],
            "portal_id": r[5],
            "portal_nombre": r[6],
            "tematica_id": r[7],
            "tematica_nombre": r[8],
            "autor": r[9],
            "interaccion_id": r[10],
            "fecha_leido": r[11],
            "utilidad": r[12],
            "resumen_claro": r[13]
        }
        for r in result
    ]
    return resultados

