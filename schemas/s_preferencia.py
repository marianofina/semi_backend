from pydantic import BaseModel


class PreferenciaBase(BaseModel):
    tematica_id: int
    interesa: bool


class PreferenciaMostrar(PreferenciaBase):
    id: int

    class Config:
        from_attributes = True


class PreferenciaView(BaseModel):
    id: int
    nombre: str
    interesa: bool
