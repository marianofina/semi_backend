from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class NoticiaBase(BaseModel):
    titulo: str
    contenido: str
    portal_id: int
    tematica_id: int
    autor: Optional[str]

    class Config:
        from_attributes = True


class NoticiaLista(BaseModel):
    id: int
    titulo: str
    nivel_resumen: Optional[float]  # Puede venir NULL
    fecha_publicacion: datetime
    url_original: Optional[str]
    portal_id: int
    portal_nombre: str
    tematica_id: int
    tematica_nombre: str
    autor: Optional[str]  # Puede venir NULL
    interaccion_id: Optional[int]  # LEFT JOIN → puede ser None
    fecha_leido: Optional[datetime]
    utilidad: Optional[int]
    resumen_claro: Optional[int]
    contenido: str

    class Config:
        from_attributes = True  # Pydantic v2 (antes orm_mode = True)


class NoticiaView(NoticiaLista):
    resumen: Optional[str]


class NoticiaOut(NoticiaBase):
    id: int
    fecha_publicacion: datetime
    carga: int

    class Config:
        from_attributes = True


