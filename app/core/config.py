import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
        # Em produção, as variáveis de ambiente devem ser definidas no ambiente de execução.
        # O arquivo .env é mais para desenvolvimento local.

settings = Settings()