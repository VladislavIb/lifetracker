import os
from pathlib import Path
from typing import Optional

from pydantic_settings import BaseSettings
from dotenv import load_dotenv


BASE_DIR_OUT = Path(__file__).resolve().parent.parent
BASE_DIR_PROJECT = BASE_DIR_OUT.parent
ENV_FILE_PATH = BASE_DIR_OUT / 'infra' / '.env'

if os.getenv('DEBUG', 'False') == 'True':
    load_dotenv(ENV_FILE_PATH)


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

    @property
    def database_url(self) -> str:
        """Формирует URL для подключения к БД."""
        return (
            f'{self.DB_DRIVE}://'
            f'{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@'
            f'{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}'
        )

    class Config:
        """Конфигурация класса."""

        env_file = ENV_FILE_PATH
        extra = 'ignore'
