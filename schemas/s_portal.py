from pydantic import BaseModel
from typing import Optional


class PortalBase(BaseModel):
    nombre: str
    logo: Optional[str]
    url_base: str


class PortalCreate(PortalBase):
    pass


class PortalOut(PortalBase):
    id: int

    class Config:
        orm_mode = True
