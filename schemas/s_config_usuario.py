from pydantic import BaseModel, condecimal, validator, field_validator
from typing import Optional


class ConfigUsuario(BaseModel):
    notificaciones_activadas: Optional[bool]
    nivel_resumen: condecimal(max_digits=3, decimal_places=2)

    @field_validator("nivel_resumen")
    @classmethod
    def validar_nivel(cls, v):
        if float(v) not in [0.2, 0.5, 0.8]:
            raise ValueError("nivel_resumen debe ser 0.2, 0.5 o 0.8")
        return v


class ConfigUsuarioGet(ConfigUsuario):
    id: int
    usuario_id: int
