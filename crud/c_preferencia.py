from models.m_preferencia import Preferencia
from sqlalchemy import text


def crear_preferencia(db, usuario_id: int, tematica_id: int, interesa: bool):
    pref = obtener_preferencia(db, usuario_id, tematica_id)
    if pref:
        pref.tematica_id = tematica_id
        pref.interesa = interesa
        db.commit()
        db.refresh(pref)
    else:
        pref = Preferencia(usuario_id=usuario_id, tematica_id=tematica_id, interesa=interesa)
        db.add(pref)
        db.commit()
        db.refresh(pref)
    return pref


def listar_preferencias(db, usuario_id):
    return db.query(Preferencia).filter(Preferencia.usuario_id == usuario_id, Preferencia.interesa == 1).all()


def obtener_preferencia(db, usuario_id: int, tematica_id: int):
    return db.query(Preferencia).filter(Preferencia.tematica_id == tematica_id, Preferencia.usuario_id == usuario_id).first()


def listar_preferencias_total_usuario(db, usuario_id: int):
    result = db.execute(
        text("EXEC preferencias_tot_usuario @id_usuario = :usuario_id"),
        {"usuario_id": usuario_id}
    ).fetchall()
    return [
        {"id": row[0], "nombre": row[1], "interesa": row[2]}
        for row in result
    ]

