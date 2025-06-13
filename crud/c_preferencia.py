from models.m_preferencia import Preferencia


def crear_preferencia(db, usuario_id: int, tematica_id: int, interesa: bool):
    pref = Preferencia(usuario_id=usuario_id, tematica_id=tematica_id, interesa=interesa)
    db.add(pref)
    db.commit()
    db.refresh(pref)
    return pref


def listar_preferencias(db, usuario_id):
    return db.query(Preferencia).filter(Preferencia.usuario_id == usuario_id, Preferencia.interesa == 1).all()
