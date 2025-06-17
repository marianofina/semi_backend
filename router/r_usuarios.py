from fastapi import APIRouter, Depends, HTTPException, status, Response
from jose import jwt
from sqlalchemy.orm import Session
from schemas.s_usuario import UsuarioCreate, UsuarioOut, Token, UsuarioBase, UsuarioActual
from crud.c_usuario import crear_usuario, autenticar_usuario
from auth import create_access_token, obtener_usuario_desde_cookie
from database import get_db
import datetime
from auth import SECRET_KEY, ALGORITHM

router = APIRouter()


@router.post("/register", response_model=UsuarioOut)
def register(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    existente = crear_usuario(db, usuario)
    return existente


@router.get("/yo", response_model=UsuarioActual)
def auth(user_id: int = Depends(obtener_usuario_desde_cookie)):
    if not user_id:
        raise HTTPException(status_code=400, detail="Credenciales inválidas")
    return {'user_id': user_id}


@router.post("/login")
def login(form: UsuarioBase, response: Response, db: Session = Depends(get_db)):
    usuario = autenticar_usuario(db, form.username, form.password)
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    # Generar JWT
    payload = {
        "id": usuario.id,
        "sub": form.username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    # Guardar token en cookie
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,  # Evita acceso por JS (más seguro)
        samesite="lax",  # Cambiar a 'strict' o 'none' según el uso
        secure=False  # True si usás HTTPS
    )
    return {"mensaje": "Login exitoso"}
