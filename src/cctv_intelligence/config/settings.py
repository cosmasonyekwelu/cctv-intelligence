from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os


@dataclass(frozen=True)
class Settings:
    app_name: str
    app_env: str
    log_level: str
    api_host: str
    api_port: int
    database_path: Path



def _env(name: str, default: str) -> str:
    return os.getenv(name, default).strip()



def load_settings() -> Settings:
    database_path = Path(_env("DATABASE_PATH", "./data/cctv_intelligence.db")).expanduser().resolve()
    return Settings(
        app_name=_env("APP_NAME", "cctv-intelligence"),
        app_env=_env("APP_ENV", "development"),
        log_level=_env("LOG_LEVEL", "INFO"),
        api_host=_env("API_HOST", "127.0.0.1"),
        api_port=int(_env("API_PORT", "8000")),
        database_path=database_path,
    )
