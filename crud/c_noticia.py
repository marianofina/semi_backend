from sqlalchemy.orm import Session
from models.m_noticia import Noticia
from schemas.s_noticia import NoticiaBase
from crud.c_preferencia import listar_preferencias
from crud.c_port_bloq import obtener_portales_bloq
from sqlalchemy import text
from services.TextTransformer import resumir
from datetime import datetime


def crear_noticia(db: Session, noticia: NoticiaBase):
    db_noticia = Noticia(
        titulo=noticia.titulo,
        contenido=noticia.contenido,
        portal_id=noticia.portal_id,
        tematica_id=noticia.tematica_id,
        autor=noticia.autor,
        fecha_publicacion=datetime.now()
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
    print(r)
    resultado = {
            "id": r[0],
            "titulo": r[1],
            "contenido": r[2],
            "resumen": resumir(r[2], r[14]) if r[14] is not None else None,
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
            "resumen_claro": r[13],
            "nivel_resumen": r[14]
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
            "fecha_publicacion": r[2],
            "url_original": r[3],
            "portal_id": r[4],
            "portal_nombre": r[5],
            "tematica_id": r[6],
            "tematica_nombre": r[7],
            "autor": r[8],
            "interaccion_id": r[9],
            "fecha_leido": r[10],
            "utilidad": r[11],
            "resumen_claro": r[12],
            "nivel_resumen": r[13],
            "contenido": r[14]
        }
        for r in result
    ]
    return resultados

