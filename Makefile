# ==============================================================================
# Campus Management System (EduCore) - Universal Makefile
# ==============================================================================

.PHONY: help install build run dev test lint clean migrate seed docker-up docker-down

PYTHON ?= python
NPM ?= npm

help:
	@echo "Campus Management System (EduCore) - Make Targets:"
	@echo "  make install     - Install both backend and frontend dependencies"
	@echo "  make build       - Build frontend assets and run collectstatic"
	@echo "  make run         - Run Django backend server on 127.0.0.1:8000"
	@echo "  make dev         - Run development servers (backend and frontend)"
	@echo "  make test        - Run full Pytest test suite"
	@echo "  make lint        - Run linters for backend and frontend"
	@echo "  make migrate     - Run database migrations"
	@echo "  make seed        - Populate demo dataset for all roles"
	@echo "  make docker-up   - Start multi-container Docker cluster"
	@echo "  make docker-down - Stop Docker containers"
	@echo "  make clean       - Remove cached bytecode, builds, and artifacts"

install:
	$(PYTHON) -m pip install -r backend/requirements.txt
	cd frontend && $(NPM) install

build:
	cd frontend && $(NPM) run build
	$(PYTHON) backend/manage.py collectstatic --noinput

run:
	$(PYTHON) main.py runserver --host 127.0.0.1 --port 8000

dev:
	$(PYTHON) main.py runserver &
	cd frontend && $(NPM) run dev

test:
	$(PYTHON) main.py test -v

lint:
	$(PYTHON) -m flake8 backend/ || true

migrate:
	$(PYTHON) main.py migrate

seed:
	$(PYTHON) main.py seed

docker-up:
	docker compose up -d --build

docker-down:
	docker compose down

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	rm -rf .pytest_cache/ htmlcov/ .coverage frontend/dist/
