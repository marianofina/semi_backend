from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from auth import obtener_usuario_desde_cookie
from crud import c_noticia as crud
from schemas import s_noticia as schemas
from database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.NoticiaBase)
def crear_noticia(noticia: schemas.NoticiaBase, db: Session = Depends(get_db)):
    return crud.crear_noticia(db, noticia)


@router.get("/", response_model=list[schemas.NoticiaBase])
def listar_noticias(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.obtener_noticias(db, skip=skip, limit=limit)


@router.get("/por-id/{noticia_id}", response_model=schemas.NoticiaView)
def obtener_noticia(noticia_id: int, db: Session = Depends(get_db), usuario_id: int = Depends(obtener_usuario_desde_cookie)):
    db_noticia = crud.obtener_noticia(db, usuario_id, noticia_id)
    if db_noticia is None:
        raise HTTPException(status_code=404, detail="Noticia no encontrada")
    return db_noticia


@router.get("/por-usuario", response_model=list[schemas.NoticiaLista])
def listar_noticias(db: Session = Depends(get_db), user_id: int = Depends(obtener_usuario_desde_cookie)):
    return crud.obtener_noticias_por_usuario(db, user_id)

"""
@router.put("/{noticia_id}", response_model=schemas.NoticiaBase)
def actualizar_noticia(noticia_id: int, noticia: schemas.NoticiaUpdate, db: Session = Depends(get_db)):
    db_noticia = crud.actualizar_noticia(db, noticia_id, noticia)
    if db_noticia is None:
        raise HTTPException(status_code=404, detail="Noticia no encontrada")
    return db_noticia


@router.delete("/{noticia_id}")
def eliminar_noticia(noticia_id: int, db: Session = Depends(get_db)):
    eliminado = crud.eliminar_noticia(db, noticia_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Noticia no encontrada")
    return {"mensaje": "Noticia eliminada correctamente"}
"""
