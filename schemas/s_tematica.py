from pydantic import BaseModel


class TematicaBase(BaseModel):
    nombre: str


class Tematica(TematicaBase):
    id: int

    class Config:
        from_attributes = True


class TematicaCreate(TematicaBase):
    pass
