from models.m_port_bloq import PortalBloqueado
from sqlalchemy import text


def crear_port_bloq(db, usuario_id: int, port_id: int, bloq: bool):
    port_bloq = obtener_portal_bloq(db, usuario_id, port_id)
    if port_bloq:
        port_bloq.bloq = bloq
        db.commit()
        db.refresh(port_bloq)
    else:
        port_bloq = PortalBloqueado(usuario_id=usuario_id, portal_id=port_id, bloq=bloq)
        db.add(port_bloq)
        db.commit()
        db.refresh(port_bloq)
    return port_bloq


def obtener_portales_bloq(db, usuario_id: int):
    return db.query(PortalBloqueado).filter(
        PortalBloqueado.usuario_id == usuario_id,
        PortalBloqueado.bloq == True
    ).all()


def obtener_portal_bloq(db, usuario_id: int, portal_id: int):
    return db.query(PortalBloqueado).filter(
        PortalBloqueado.usuario_id == usuario_id,
        PortalBloqueado.portal_id == portal_id
    ).first()


def obtener_portales_bloq_totales(db, usuario_id: int):
    result = db.execute(
        text("EXEC portales_total_bloq @usuario_id = :usuario_id"),
        {"usuario_id": usuario_id}
    ).fetchall()
    return [
        {"id": row[0], "nombre": row[1], "logo": row[2], "url_base": row[3], "bloqueado": row[4]}
        for row in result
    ]
