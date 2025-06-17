from pydantic import BaseModel


class AdminBase(BaseModel):
    username: str


class AdminCreate(AdminBase):
    password: str


class AdminLogin(AdminBase):
    password: str


class AdminOut(AdminBase):
    id: int

    class Config:
        from_attributes = True
