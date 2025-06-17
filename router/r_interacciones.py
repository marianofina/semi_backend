from fastapi import APIRouter, Depends
import crud.c_interaccion as crud
from auth import obtener_usuario_desde_cookie
from schemas.s_interaccion import InteraccionBase, InteraccionUtilidad, InteraccionResumen
from sqlalchemy.orm import Session
from database import get_db


router = APIRouter()


@router.post("/")
def crear_interaccion(interaccion: InteraccionBase, db: Session = Depends(get_db), user_id: int = Depends(obtener_usuario_desde_cookie)):
    return crud.crearInteracion(db, user_id, interaccion.noticia_id)


@router.put("/utilidad")
def marcar_utilidad(interaccion: InteraccionUtilidad, db: Session = Depends(get_db), user_id: int = Depends(obtener_usuario_desde_cookie)):
    if interaccion.utilidad not in [1, 2, 3, 4, 5]:
        raise ValueError("La utilidad debe ser de 1 a 5")
    return crud.update_utilidad(db, user_id, interaccion.noticia_id, interaccion.utilidad)


@router.put("/resumen_claro")
def marcar_resumen_claro(interaccion: InteraccionResumen, db: Session = Depends(get_db), user_id: int = Depends(obtener_usuario_desde_cookie)):
    if interaccion.resumen_claro not in [1, 2, 3, 4, 5]:
        raise ValueError("El resumen claro debe ser de 1 a 5")
    return crud.update_resumen_claro(db, user_id, interaccion.noticia_id, interaccion.resumen_claro)

