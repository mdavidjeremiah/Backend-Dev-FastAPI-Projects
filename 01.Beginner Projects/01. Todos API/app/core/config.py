from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = 'To-Do List API'
    DEBUG: bool = True
    DATABASE_URL: str = "sqlite:///./todos.db"

    class Config:
        env_file = ".env"

    settings = Settings()