from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from auth import obtener_usuario_desde_cookie
from schemas.s_preferencia import PreferenciaBase, PreferenciaMostrar, PreferenciaView
import crud.c_preferencia as crud

router = APIRouter()


@router.post("/", response_model=PreferenciaMostrar)
def crear_preferencia(preferencia: PreferenciaBase, db: Session = Depends(get_db), user_id: int = Depends(obtener_usuario_desde_cookie)):
    return crud.crear_preferencia(db, user_id, preferencia.tematica_id, preferencia.interesa)


@router.get("/", response_model=list[PreferenciaMostrar])
def obtener_preferencias(db: Session = Depends(get_db), user_id: int = Depends(obtener_usuario_desde_cookie)):
    return crud.listar_preferencias(db, user_id)


@router.get("/total", response_model=list[PreferenciaView])
def obtener_preferencias_totales_usuario(db: Session = Depends(get_db), user_id: int = Depends(obtener_usuario_desde_cookie)):
    return crud.listar_preferencias_total_usuario(db, user_id)
