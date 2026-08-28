#!/bin/sh
set -e

echo "==> Running Campus Management Backend Entrypoint..."

# Wait for PostgreSQL if DB_HOST is set and not sqlite
if [ "$DB_ENGINE" != "django.db.backends.sqlite3" ] && [ -n "$DB_HOST" ]; then
    echo "==> Waiting for PostgreSQL database at ${DB_HOST}:${DB_PORT:-5432}..."
    while ! nc -z "$DB_HOST" "${DB_PORT:-5432}"; do
      sleep 1
    done
    echo "==> PostgreSQL is up and accepting connections!"
fi

echo "==> Applying database migrations..."
python manage.py migrate --noinput

echo "==> Collecting static files..."
python manage.py collectstatic --noinput --clear || true

exec "$@"
