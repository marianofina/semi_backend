from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import (r_usuarios,
                    r_noticias,
                    r_interacciones,
                    r_portal,
                    r_tematica,
                    r_preferencia,
                    r_port_bloq)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # dominio del front
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(r_usuarios.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(r_port_bloq.router, prefix="/protected/portales-bloq", tags=["Portales Bloqueados"])
# app.include_router(r_admins.router, prefix="/admins", tags=["Admins"])
app.include_router(r_noticias.router, prefix="/noticias", tags=["Noticias"])
app.include_router(r_interacciones.router, prefix="/protected/interacciones", tags=["Interacciones"])
app.include_router(r_tematica.router, prefix="/tematicas", tags=["Temáticas"])
app.include_router(r_portal.router, prefix="/portales", tags=["Portales"])
app.include_router(r_preferencia.router, prefix="/protected/preferencias", tags=["Portales"])
