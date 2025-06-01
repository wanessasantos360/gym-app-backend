from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependência para obter a sessão da base de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Função para inicializar a base de dados (criar tabelas)
# Em produção, use Alembic para migrações.
def init_db():
    # Importar todos os modelos aqui para que sejam registados com o SQLAlchemy Base
    # antes de criar as tabelas.
    from app.models import user_model, exercise_definition_model, workout_model
    Base.metadata.create_all(bind=engine)
