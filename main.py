from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import (r_usuarios,
                    r_noticias,
                    r_interacciones,
                    r_portal,
                    r_tematica,
                    r_preferencia,
                    r_port_bloq,
                    test_text_transformer,
                    r_config_usuario
                    )

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
app.include_router(r_config_usuario.router, prefix="/protected", tags=["Configuración Usuario"])
app.include_router(test_text_transformer.router, prefix="/resumen", tags=["Resumen IA"])
app.include_router(r_noticias.router, prefix="/noticias", tags=["Noticias"])
app.include_router(r_interacciones.router, prefix="/protected/interacciones", tags=["Interacciones"])
app.include_router(r_tematica.router, prefix="/tematicas", tags=["Temáticas"])
app.include_router(r_portal.router, prefix="/portales", tags=["Portales"])
app.include_router(r_preferencia.router, prefix="/protected/preferencias", tags=["Portales"])
