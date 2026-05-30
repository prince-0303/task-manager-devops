# Task Manager DevOps

A production-ready REST API built to demonstrate full-stack backend 
and DevOps engineering practices.

## Tech Stack

- **Backend** — Django 6 + Django REST Framework
- **Auth** — JWT via SimpleJWT
- **Database** — PostgreSQL
- **Containerization** — Docker + Docker Compose
- **CI/CD** — GitHub Actions
- **Deployment** — AWS EC2
- **Web Server** — Nginx + Gunicorn
- **SSL** — Certbot (Let's Encrypt)

## Features

- JWT Authentication (access + refresh tokens)
- Full CRUD Task Management API
- User-scoped tasks (users only see their own tasks)
- Dockerized development environment
- Automated CI/CD pipeline
- Production deployment on AWS

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/token/` | Get JWT tokens |
| POST | `/api/token/refresh/` | Refresh access token |
| GET | `/api/tasks/` | List all your tasks |
| POST | `/api/tasks/` | Create a task |
| GET | `/api/tasks/:id/` | Get a task |
| PUT | `/api/tasks/:id/` | Update a task |
| DELETE | `/api/tasks/:id/` | Delete a task |

## Local Development

### Prerequisites
- Docker
- Docker Compose

### Setup

1. Clone the repo
```bash
   git clone https://github.com/YOUR_USERNAME/task-manager-devops.git
   cd task-manager-devops
```

2. Create your env file
```bash
   cp .env.example .env
```

3. Start the containers
```bash
   docker compose up --build
```

4. Run migrations
```bash
   docker compose exec web python manage.py migrate
```

5. Create superuser
```bash
   docker compose exec web python manage.py createsuperuser
```

6. Hit the API at `http://localhost:8000`

## Architecture

```
Developer → GitHub → GitHub Actions → AWS EC2
                                          │
                                     Nginx (80/443)
                                          │
                                     Gunicorn (8000)
                                          │
                                     Django + DRF
                                          │
                                     PostgreSQL
```