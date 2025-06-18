from fastapi import APIRouter, Depends
from crud.c_config_usuario import obtener_config_usuario, crearConfigUsuario
from auth import obtener_usuario_desde_cookie
from schemas.s_config_usuario import ConfigUsuario
from sqlalchemy.orm import Session
from database import get_db


router = APIRouter()


@router.get("/config-usuario")
def get_config_usuario(db: Session = Depends(get_db), user_id: int = Depends(obtener_usuario_desde_cookie)):
    return obtener_config_usuario(db, user_id)


@router.post("/config-usuario")
def post_config_usuario(config: ConfigUsuario, db: Session = Depends(get_db), user_id: int = Depends(obtener_usuario_desde_cookie)):
    return crearConfigUsuario(db, user_id, notificaciones_activadas=config.notificaciones_activadas, nivel_resumen=config.nivel_resumen)
