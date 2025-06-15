from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from auth import obtener_usuario_desde_cookie
import crud.c_port_bloq as crud
from schemas.s_port_bloq import PortBloqBase

router = APIRouter()


@router.post("/")
def crear_port_bloq(portBloq: PortBloqBase, db: Session = Depends(get_db), user_id: int = Depends(obtener_usuario_desde_cookie)):
    return crud.crear_port_bloq(db, user_id, portBloq.portal_id, portBloq.bloq)
