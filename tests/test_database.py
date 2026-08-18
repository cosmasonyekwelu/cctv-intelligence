from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from cctv_intelligence.storage.database import connect
from cctv_intelligence.storage.migrations import run_migrations


class DatabaseTests(unittest.TestCase):
    def test_run_migrations_creates_events_table(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        migrations_dir = repo_root / "migrations"

        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = Path(temp_dir) / "test.db"
            with connect(db_path) as connection:
                run_migrations(connection, migrations_dir)
                row = connection.execute(
                    "SELECT name FROM sqlite_master WHERE type='table' AND name='events'"
                ).fetchone()

            self.assertIsNotNone(row)
