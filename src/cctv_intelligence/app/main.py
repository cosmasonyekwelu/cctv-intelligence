from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import logging

from cctv_intelligence.api.http import create_health_app
from cctv_intelligence.config.settings import Settings, load_settings
from cctv_intelligence.observability.logging import configure_logging
from cctv_intelligence.storage.database import connect
from cctv_intelligence.storage.migrations import run_migrations


@dataclass
class Application:
    settings: Settings
    wsgi_app: object



def build_application(migrations_dir: Path | None = None) -> Application:
    settings = load_settings()
    configure_logging(settings.log_level)

    with connect(settings.database_path) as connection:
        run_migrations(connection, migrations_dir or Path("migrations"))

    logging.getLogger(__name__).info("application_initialized", extra={"environment": settings.app_env})

    return Application(
        settings=settings,
        wsgi_app=create_health_app(settings.app_name),
    )
