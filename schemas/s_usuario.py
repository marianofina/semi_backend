from pydantic import BaseModel
from datetime import date


class UsuarioBase(BaseModel):
    username: str
    password: str


class UsuarioCreate(UsuarioBase):
    fecha_nac: date


class UsuarioOut(UsuarioBase):
    id: int


class Token(BaseModel):
    access_token: str
    token_type: str
