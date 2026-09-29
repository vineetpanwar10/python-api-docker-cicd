![CI](https://github.com/vineetpanwar10/python-api-docker-cicd/actions/workflows/ci.yml/badge.svg)
# Python API - Docker & CI/CD

A small Task REST API built with Python and FastAPI.

## What this project demonstrates

- Python REST API
- Git/GitHub workflow
- Docker image and container
- Docker port mapping
- Environment variables
- Automated tests
- GitHub Actions CI workflow

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

## Run with Docker

Build:

```bash
docker build -t task-api .
```

Run:

```bash
docker run -p 8000:8000 -e APP_ENV=docker task-api
```

Open:

```text
http://127.0.0.1:8000
```

## API examples

Get tasks:

```text
GET /tasks
```

Create a task:

```text
POST /tasks
```

JSON body:

```json
{
  "title": "Learn Docker"
}
```

## Run tests

```bash
pytest
```

GitHub Actions runs the tests and builds the Docker image automatically on push or pull request.
