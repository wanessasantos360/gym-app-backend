from fastapi import FastAPI
from app.db.database import init_db # Função para criar tabelas (apenas para desenvolvimento)
# from app.apis.v1 import api_router # A ser implementado para routers modulares

# Chamar init_db() para criar as tabelas na base de dados ao iniciar a aplicação.
# ATENÇÃO: Em produção, deve usar Alembic para gerir migrações da base de dados.
# Comentado por agora, pois o Alembic será a abordagem preferida.
# init_db()

app = FastAPI(
    title="Gym App API MVP",
    description="API para o MVP da Aplicação de Registo de Treinos de Ginásio.",
    version="0.1.0"
)

# Incluir routers da API (a ser implementado)
# from app.apis.v1.endpoints import auth_router, users_router, workouts_router # Exemplo
# app.include_router(auth_router.router, prefix="/api/v1/auth", tags=["Auth"])
# app.include_router(users_router.router, prefix="/api/v1/users", tags=["Users"])
# app.include_router(workouts_router.router, prefix="/api/v1/workouts", tags=["Workouts"])


@app.on_event("startup")
async def on_startup():
    # Esta é uma alternativa para chamar init_db() ou outras lógicas de inicialização.
    # Para o MVP, a criação de tabelas pode ser feita aqui ou manualmente com Alembic.
    # Se usar Alembic, esta chamada init_db() não é estritamente necessária após a primeira migração.
    print("A iniciar a aplicação API...")
    # init_db() # Descomente se quiser criar tabelas na inicialização sem Alembic


@app.get("/")
async def root():
    """
    Endpoint raiz da API.
    """
    return {"message": "Bem-vindo à API MVP do Gym App!"}

@app.get("/health", tags=["Health Check"])
async def health_check():
    """
    Verifica a saúde da API.
    """
    return {"status": "saudável", "message": "API está a funcionar corretamente!"}

# Endpoints de exemplo e CRUD serão movidos para os seus próprios routers/módulos.
