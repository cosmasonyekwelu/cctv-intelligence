from __future__ import annotations

from json import dumps
from typing import Callable



def create_health_app(app_name: str) -> Callable:
    def application(environ, start_response):
        method = environ.get("REQUEST_METHOD", "GET")
        path = environ.get("PATH_INFO", "/")

        if method == "GET" and path == "/health":
            body = dumps({"status": "ok", "service": app_name}).encode("utf-8")
            headers = [
                ("Content-Type", "application/json"),
                ("Content-Length", str(len(body))),
            ]
            start_response("200 OK", headers)
            return [body]

        body = b"Not Found"
        start_response("404 Not Found", [("Content-Type", "text/plain"), ("Content-Length", str(len(body)))])
        return [body]

    return application
