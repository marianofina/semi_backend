from pydantic import BaseModel


class TematicaBase(BaseModel):
    nombre: str


class TematicaCreate(TematicaBase):
    pass


class Tematica(TematicaBase):
    id: int

    class Config:
        orm_mode = True
