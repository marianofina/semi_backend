from typing import Optional

from pydantic import BaseModel


class PortBloqBase(BaseModel):
    portal_id: int
    bloq: bool


class PortalBloqView(BaseModel):
    id: int
    nombre: str
    logo: Optional[str]
    url_base: str
    bloqueado: bool
