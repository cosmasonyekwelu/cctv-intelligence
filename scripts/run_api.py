from __future__ import annotations

from wsgiref.simple_server import make_server

from cctv_intelligence.app.main import build_application


if __name__ == "__main__":
    application = build_application()
    server = make_server(application.settings.api_host, application.settings.api_port, application.wsgi_app)
    print(f"Serving on http://{application.settings.api_host}:{application.settings.api_port}")
    server.serve_forever()
