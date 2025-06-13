from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud.c_tematica as crud
import schemas.s_tematica as schemas
from database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Tematica)
def crear_tematica(tematica: schemas.TematicaCreate, db: Session = Depends(get_db)):
    return crud.crear_tematica(db, tematica)


@router.get("/", response_model=list[schemas.Tematica])
def listar_tematicas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.listar_tematicas(db, skip, limit)


@router.get("/{tematica_id}", response_model=schemas.Tematica)
def obtener_tematica(tematica_id: int, db: Session = Depends(get_db)):
    tematica = crud.obtener_tematica(db, tematica_id)
    if not tematica:
        raise HTTPException(status_code=404, detail="Temática no encontrada")
    return tematica


@router.delete("/{tematica_id}", response_model=schemas.Tematica)
def eliminar_tematica(tematica_id: int, db: Session = Depends(get_db)):
    tematica = crud.eliminar_tematica(db, tematica_id)
    if not tematica:
        raise HTTPException(status_code=404, detail="Temática no encontrada")
    return tematica
