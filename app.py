"""
Campus Management System (EduCore) - Application Orchestrator

Serves as the root application entry point for WSGI/ASGI application mounting,
background task worker initialization, and multi-service process orchestration.
"""

import os
import sys
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("EduCore.App")

# Add backend to Python path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, "backend")
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


def get_wsgi_application():
    """Load and return the Django WSGI application instance."""
    from django.core.wsgi import get_wsgi_application as _get_wsgi
    return _get_wsgi()


def get_asgi_application():
    """Load and return the Django ASGI application instance."""
    from django.core.asgi import get_asgi_application as _get_asgi
    return _get_asgi()


def run_standalone(host: str = "0.0.0.0", port: int = 8000) -> None:
    """Start standalone WSGI server with gunicorn or wsgiref."""
    import django
    django.setup()
    from wsgiref.simple_server import make_server

    app = get_wsgi_application()
    logger.info("EduCore Application Server listening on http://%s:%d", host, port)
    server = make_server(host, port, app)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logger.info("Server shutdown requested by user.")


def init_app_context() -> Dict[str, Any]:
    """Initialize core application services, caches, and database pools."""
    import django
    django.setup()
    from django.conf import settings
    logger.info("Initializing EduCore context in %s mode", "DEBUG" if settings.DEBUG else "PRODUCTION")
    return {
        "debug": settings.DEBUG,
        "installed_apps": len(settings.INSTALLED_APPS),
        "timezone": settings.TIME_ZONE,
        "database_engine": settings.DATABASES["default"]["ENGINE"]
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    host = os.environ.get("HOST", "0.0.0.0")
    run_standalone(host=host, port=port)
