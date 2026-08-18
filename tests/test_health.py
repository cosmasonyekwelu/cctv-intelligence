from __future__ import annotations

import unittest

from cctv_intelligence.api.http import create_health_app


class HealthEndpointTests(unittest.TestCase):
    def test_health_endpoint_returns_ok(self) -> None:
        app = create_health_app("cctv-intelligence")
        status_holder = {}

        def start_response(status, headers):
            status_holder["status"] = status
            status_holder["headers"] = headers

        response_chunks = app(
            {"REQUEST_METHOD": "GET", "PATH_INFO": "/health"},
            start_response,
        )
        body = b"".join(response_chunks).decode("utf-8")

        self.assertEqual(status_holder["status"], "200 OK")
        self.assertIn('"status": "ok"', body)
