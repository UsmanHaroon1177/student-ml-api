# student-ml-api

A simple ML inference API built to demonstrate a professional MLOps CI/CD workflow — feature branches, pull-request-gated merges, automated testing, Dockerization, and versioned publishing to a container registry.

## What it does

The API accepts a numeric value and returns a prediction. Endpoints:

**`GET /health`**
```json
{
  "status": "healthy",
  "application": "student-ml-api",
  "application_version": "1.1.0",
  "model_version": "model-1"
}
```

**`POST /predict`**
```json
// Request
{ "value": 10 }

// Response
{ "input": 10, "prediction": 20 }
```

## Running locally

```bash
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 5000
```

Then:
```bash
curl http://localhost:5000/health
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"value": 10}'
```

## Running the tests

```bash
pytest -v
```

## Running with Docker

Pull the published image from GitHub Container Registry instead of building locally:
```bash
docker pull ghcr.io/usmanharoon1177/student-ml-api:latest
docker run -d --name student-ml-api -p 5000:5000 ghcr.io/usmanharoon1177/student-ml-api:latest
curl http://localhost:5000/health
```

Or build it yourself:
```bash
docker build -t student-ml-api:local .
docker run -d --name student-ml-api -p 5000:5000 student-ml-api:local
```

## CI/CD Workflow

- **`.github/workflows/ci.yml`** — runs on every pull request into `main`. Installs dependencies, runs the test suite, and validates that the Docker image builds. Does not publish anything.
- **`.github/workflows/release.yml`** — runs only when a semantic version tag (`v*.*.*`) is pushed. Re-runs tests, builds the Docker image, and publishes it to GHCR tagged with the version number, `latest`, and the triggering commit SHA.

`main` is protected — all changes go through a pull request and must pass CI before merging.

## Versions published

| Tag | Notes |
|---|---|
| `1.0.0` | Initial release — `/health` and `/predict` |
| `1.1.0` | Adds `application_version` and `model_version` to `/health` |
| `latest` | Always points to the newest release |

## Tech stack

FastAPI, pytest, Docker, GitHub Actions, GitHub Container Registry (GHCR)
