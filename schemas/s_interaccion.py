from pydantic import BaseModel


class InteraccionBase(BaseModel):
    noticia_id: int


class InteraccionUtilidad(InteraccionBase):
    utilidad: int


class InteraccionResumen(InteraccionBase):
    resumen_claro: int
