from __future__ import annotations

import os
import tempfile
import unittest

from cctv_intelligence.config.settings import load_settings


class SettingsTests(unittest.TestCase):
    def test_load_settings_uses_environment_values(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            os.environ["APP_NAME"] = "test-app"
            os.environ["API_PORT"] = "9000"
            os.environ["DATABASE_PATH"] = f"{temp_dir}/test.db"

            settings = load_settings()

            self.assertEqual(settings.app_name, "test-app")
            self.assertEqual(settings.api_port, 9000)
            self.assertTrue(str(settings.database_path).endswith("test.db"))
