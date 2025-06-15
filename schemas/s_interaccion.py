from pydantic import BaseModel
from typing import Optional


class InteraccionBase(BaseModel):
    noticia_id: int
    utilidad: Optional[int]
    resumen_claro: Optional[int]
