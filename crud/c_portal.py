from sqlalchemy.orm import Session
from models.m_portal import PortalNoticia
from schemas.s_portal import PortalCreate


def crear_portal(db: Session, portal: PortalCreate):
    db_portal = PortalNoticia(
        nombre=portal.nombre,
        logo=portal.logo,
        url_base=portal.url_base
    )
    db.add(db_portal)
    db.commit()
    db.refresh(db_portal)
    return db_portal


def listar_portales(db: Session, skip: int = 0):
    return db.query(PortalNoticia).order_by(PortalNoticia.id).offset(skip).all()

