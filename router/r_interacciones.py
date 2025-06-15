from fastapi import APIRouter, Depends
import crud.c_interaccion as crud
from auth import obtener_usuario_desde_cookie
from schemas.s_interaccion import InteraccionBase
from sqlalchemy.orm import Session
from database import get_db


router = APIRouter()


@router.post("/")
def crear_interaccion(interaccion: InteraccionBase, db: Session = Depends(get_db), user_id: int = Depends(obtener_usuario_desde_cookie)):
    return crud.crearInteracion(db, user_id, interaccion.noticia_id)
