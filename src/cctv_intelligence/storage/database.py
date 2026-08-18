from __future__ import annotations

from pathlib import Path
import sqlite3



def ensure_parent_directory(db_path: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)



def connect(db_path: Path) -> sqlite3.Connection:
    ensure_parent_directory(db_path)
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    return connection
