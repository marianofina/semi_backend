from models.m_port_bloq import PortalBloqueado


def crear_port_bloq(db, usuario_id: int, port_id: int, bloq: bool):
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
