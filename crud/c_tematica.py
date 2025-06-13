from sqlalchemy.orm import Session
from models.m_tematica import TematicaNoticia
from schemas.s_tematica import TematicaCreate


def crear_tematica(db: Session, tematica: TematicaCreate):
    nueva_tematica = TematicaNoticia(**tematica.dict())
    db.add(nueva_tematica)
    db.commit()
    db.refresh(nueva_tematica)
    return nueva_tematica


def listar_tematicas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TematicaNoticia).order_by(TematicaNoticia.id).offset(skip).limit(limit).all()


def obtener_tematica(db: Session, tematica_id: int):
    return db.query(TematicaNoticia).filter(TematicaNoticia.id == tematica_id).first()


def eliminar_tematica(db: Session, tematica_id: int):
    tematica = db.query(TematicaNoticia).filter(TematicaNoticia.id == tematica_id).first()
    if tematica:
        db.delete(tematica)
        db.commit()
    return tematica
