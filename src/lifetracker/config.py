from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / 'infra' / '.env')


class Settings(BaseSettings):
    """Настройки приложения."""

    # TODO: Не забудь добавить в .env файл
    # переменные окружения, которые ты здесь используешь.
    DB_DRIVE: Optional[str] = 'postgresql+asyncpg'
    DB_HOST: Optional[str] = 'localhost'
    DB_PORT: Optional[int] = 5432
    POSTGRES_USER: Optional[str] = 'postgres'
    POSTGRES_PASSWORD: Optional[str] = 'postgres'
    POSTGRES_DB: Optional[str] = 'lifetracker'
    DB_ECHO: Optional[bool] = False

    model_config = SettingsConfigDict(env_file=BASE_DIR / 'infra' / '.env')

    @property
    def database_url(self) -> str:
        """Формирует URL для подключения к БД."""
        return (
            f'{self.DB_DRIVE}://'
            f'{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@'
            f'{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}'
        )


settings = Settings()
