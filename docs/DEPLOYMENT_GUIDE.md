# 🚀 Production Deployment & DevOps Engineering Guide

Step-by-step production deployment instructions using Docker Compose, Gunicorn, Nginx, PostgreSQL, Redis, and SSL/TLS.

---

## 1. Prerequisites & System Requirements

- **Operating System**: Ubuntu 22.04 LTS or enterprise Linux distribution
- **Hardware**: Minimum 4 vCPUs, 8 GB RAM, 50 GB SSD
- **Software**: Docker Engine 24+, Docker Compose v2, Git

---

## 2. Docker Compose Infrastructure (`docker-compose.yml`)

```yaml
version: '3.8'

services:
  db:
    image: postgres:16-alpine
    container_name: campus_postgres
    restart: always
    environment:
      POSTGRES_DB: campus_db
      POSTGRES_USER: campus_user
      POSTGRES_PASSWORD: secure_campus_password_2026
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  redis:
    image: redis:7-alpine
    container_name: campus_redis
    restart: always
    ports:
      - "6379:6379"

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: campus_backend
    restart: always
    command: gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 4 --threads 2
    environment:
      - DATABASE_URL=postgres://campus_user:secure_campus_password_2026@db:5432/campus_db
      - REDIS_URL=redis://redis:6379/0
      - SECRET_KEY=production_secret_key_campus_2026
      - DEBUG=False
    depends_on:
      - db
      - redis
    ports:
      - "8000:8000"

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: campus_frontend
    restart: always
    ports:
      - "80:80"
      - "443:443"

volumes:
  postgres_data:
```

---

## 3. Nginx Reverse Proxy Configuration

```nginx
server {
    listen 80;
    server_name campus.university.edu;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name campus.university.edu;

    ssl_certificate /etc/letsencrypt/live/campus.university.edu/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/campus.university.edu/privkey.pem;

    # Frontend Single Page App
    location / {
        root /usr/share/nginx/html;
        index index.html;
        try_files $uri $uri/ /index.html;
    }

    # Backend REST API
    location /api/ {
        proxy_pass http://backend:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

---

## 4. Initialization & Migration Commands

```bash
# 1. Start cluster
docker compose up -d

# 2. Run database migrations
docker compose exec backend python manage.py migrate

# 3. Seed demo accounts & curriculum benchmark
docker compose exec backend python manage.py init_demo_data

# 4. Collect static files
docker compose exec backend python manage.py collectstatic --noinput
```
