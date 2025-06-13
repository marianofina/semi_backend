from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from auth import decode_token
from database import get_db
from crud.c_usuario import get_usuario_por_email
from models.m_usuario import Usuario

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> Usuario:
    user_id = decode_token(token)
    if user_id is None:
        raise HTTPException(status_code=401, detail="Token inválido")
    usuario = db.query(Usuario).get(int(user_id))
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario
