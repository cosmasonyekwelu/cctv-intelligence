from __future__ import annotations

from pathlib import Path
import sqlite3



def apply_migration_file(connection: sqlite3.Connection, migration_path: Path) -> None:
    version = migration_path.name
    already_applied = connection.execute(
        "SELECT 1 FROM schema_migrations WHERE version = ?",
        (version,),
    ).fetchone()
    if already_applied:
        return

    sql = migration_path.read_text(encoding="utf-8")
    with connection:
        connection.executescript(sql)
        connection.execute(
            "INSERT INTO schema_migrations(version) VALUES (?)",
            (version,),
        )



def run_migrations(connection: sqlite3.Connection, migrations_dir: Path) -> None:
    bootstrap_sql = """
    CREATE TABLE IF NOT EXISTS schema_migrations (
        version TEXT PRIMARY KEY,
        applied_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """
    with connection:
        connection.executescript(bootstrap_sql)

    for migration_path in sorted(migrations_dir.glob("*.sql")):
        apply_migration_file(connection, migration_path)
