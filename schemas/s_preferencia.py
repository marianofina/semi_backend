from pydantic import BaseModel


class PreferenciaBase(BaseModel):
    tematica_id: int
    interesa: bool


class PreferenciaMostrar(PreferenciaBase):
    id: int

    class Config:
        orm_mode = True
