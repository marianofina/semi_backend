from pydantic import BaseModel


class PortBloqBase(BaseModel):
    portal_id: int
    bloq: bool