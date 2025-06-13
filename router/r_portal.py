from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas import s_portal as schemas
from crud import c_portal as crud
from database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.PortalOut)
def crear_portal(portal: schemas.PortalCreate, db: Session = Depends(get_db)):
    return crud.crear_portal(db, portal)


@router.get("/", response_model=List[schemas.PortalOut])
def listar_portales(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.listar_portales(db, skip, limit)
