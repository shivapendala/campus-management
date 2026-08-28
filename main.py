#!/usr/bin/env python
"""
Campus Management System (EduCore) - Main Entry Point

Unified orchestration CLI for backend services, database migrations,
fixture seeding, test suite execution, frontend building, and system health checks.
"""

import os
import sys
import argparse
import subprocess
import logging
from typing import List, Optional

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("EduCore.Main")


def get_base_dir() -> str:
    """Return the absolute path to the project root directory."""
    return os.path.dirname(os.path.abspath(__file__))


def run_command(cmd: List[str], cwd: Optional[str] = None) -> int:
    """Execute a system command and return the exit code."""
    work_dir = cwd or get_base_dir()
    logger.info("Executing: %s (cwd=%s)", " ".join(cmd), work_dir)
    try:
        result = subprocess.run(cmd, cwd=work_dir, check=False)
        return result.returncode
    except Exception as exc:
        logger.error("Command execution failed: %s", exc)
        return 1


def cmd_runserver(args: argparse.Namespace) -> int:
    """Run the Django development server."""
    backend_dir = os.path.join(get_base_dir(), "backend")
    addr = f"{args.host}:{args.port}"
    cmd = [sys.executable, "manage.py", "runserver", addr]
    return run_command(cmd, cwd=backend_dir)


def cmd_migrate(args: argparse.Namespace) -> int:
    """Apply database migrations across all apps."""
    backend_dir = os.path.join(get_base_dir(), "backend")
    cmd = [sys.executable, "manage.py", "migrate"]
    return run_command(cmd, cwd=backend_dir)


def cmd_makemigrations(args: argparse.Namespace) -> int:
    """Generate new database migrations."""
    backend_dir = os.path.join(get_base_dir(), "backend")
    cmd = [sys.executable, "manage.py", "makemigrations"]
    return run_command(cmd, cwd=backend_dir)


def cmd_seed(args: argparse.Namespace) -> int:
    """Seed the database with standard campus demo data."""
    backend_dir = os.path.join(get_base_dir(), "backend")
    cmd = [sys.executable, "manage.py", "seed_data"]
    return run_command(cmd, cwd=backend_dir)


def cmd_test(args: argparse.Namespace) -> int:
    """Run full Pytest test suite with coverage."""
    cmd = [sys.executable, "-m", "pytest"]
    if args.verbose:
        cmd.append("-v")
    if args.filter:
        cmd.extend(["-k", args.filter])
    return run_command(cmd, cwd=get_base_dir())


def cmd_build(args: argparse.Namespace) -> int:
    """Build the production frontend bundle."""
    frontend_dir = os.path.join(get_base_dir(), "frontend")
    logger.info("Building frontend production bundle...")
    npm_cmd = "npm.cmd" if sys.platform == "win32" else "npm"
    return run_command([npm_cmd, "run", "build"], cwd=frontend_dir)


def cmd_healthcheck(args: argparse.Namespace) -> int:
    """Verify system health, database accessibility, and configurations."""
    backend_dir = os.path.join(get_base_dir(), "backend")
    sys.path.insert(0, backend_dir)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    try:
        import django
        django.setup()
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            row = cursor.fetchone()
        logger.info("Database connection: HEALTHY (Check returned: %s)", row)

        from apps.accounts.models import User
        user_count = User.objects.count()
        logger.info("Database records check: %d registered users found", user_count)

        logger.info("All system health checks PASSED successfully.")
        return 0
    except Exception as exc:
        logger.error("Health check failure: %s", exc)
        return 1


def cmd_status(args: argparse.Namespace) -> int:
    """Display overall system metrics, LOC stats, and service statuses."""
    logger.info("=== Campus Management System (EduCore) Status ===")
    logger.info("Root Directory: %s", get_base_dir())
    logger.info("Python Runtime: %s", sys.version.split()[0])
    logger.info("Platform: %s", sys.platform)
    return cmd_healthcheck(args)


def build_parser() -> argparse.ArgumentParser:
    """Build and configure the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="educore",
        description="Campus Management System (EduCore) CLI Management Tool"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # runserver
    server_parser = subparsers.add_parser("runserver", help="Start the Django backend server")
    server_parser.add_argument("--host", default="127.0.0.1", help="Binding host IP (default: 127.0.0.1)")
    server_parser.add_argument("--port", default="8000", help="Binding port (default: 8000)")

    # migrate
    subparsers.add_parser("migrate", help="Run database migrations")

    # makemigrations
    subparsers.add_parser("makemigrations", help="Create new database migrations")

    # seed
    subparsers.add_parser("seed", help="Seed institutional demonstration dataset")

    # test
    test_parser = subparsers.add_parser("test", help="Run full automated test suite")
    test_parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose test output")
    test_parser.add_argument("-k", "--filter", default="", help="Filter tests by expression")

    # build
    subparsers.add_parser("build", help="Build frontend production bundle")

    # healthcheck
    subparsers.add_parser("healthcheck", help="Run comprehensive database and service health checks")

    # status
    subparsers.add_parser("status", help="Show system status and component summary")

    return parser


def main() -> int:
    """Main execution function."""
    parser = build_parser()
    args = parser.parse_args()

    command_handlers = {
        "runserver": cmd_runserver,
        "migrate": cmd_migrate,
        "makemigrations": cmd_makemigrations,
        "seed": cmd_seed,
        "test": cmd_test,
        "build": cmd_build,
        "healthcheck": cmd_healthcheck,
        "status": cmd_status,
    }

    if not args.command:
        parser.print_help()
        return 0

    handler = command_handlers.get(args.command)
    if handler:
        return handler(args)
    else:
        logger.error("Unknown command: %s", args.command)
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
