from sqlalchemy.orm import Session
from models.m_usuario import Usuario
from auth import hash_password, verify_password


def get_usuario_por_email(db: Session, username: str):
    return db.query(Usuario).filter(Usuario.username == username).first()


def crear_usuario(db: Session, usuario_data):
    hashed_pw = hash_password(usuario_data.password)
    usuario = Usuario(username=usuario_data.username, password=hashed_pw, fecha_nac=usuario_data.fecha_nac)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario


def autenticar_usuario(db: Session, username: str, password: str):
    usuario = get_usuario_por_email(db, username)
    if usuario and verify_password(password, usuario.password):
        return usuario
    return None
