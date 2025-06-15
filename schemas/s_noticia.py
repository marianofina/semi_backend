from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class NoticiaBase(BaseModel):
    titulo: str
    contenido: str
    resumen: Optional[str]
    portal_id: int
    tematica_id: int
    autor: Optional[str]


class NoticiaCreate(NoticiaBase):
    pass


class NoticiaOut(NoticiaBase):
    id: int
    fecha_publicacion: datetime
    carga: int

    class Config:
        orm_mode = True
