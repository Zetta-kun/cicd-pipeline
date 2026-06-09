# 🔄 CI/CD Pipeline with GitHub Actions

[![CI/CD Pipeline](https://github.com/Zetta-kun/cicd-pipeline/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/Zetta-kun/cicd-pipeline/actions/workflows/ci-cd.yml)
[![Docker Pulls](https://img.shields.io/docker/pulls/zetta/cicd-pipeline)](https://hub.docker.com/r/zetta/cicd-pipeline)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

## 📌 About

Automated CI/CD pipeline using GitHub Actions. On every push:
- ✅ Runs tests automatically
- ✅ Builds Docker image
- ✅ Pushes to Docker Hub
- ✅ Ready for deployment

## 🛠️ Technologies

| Technology | Purpose |
|------------|---------|
| **GitHub Actions** | CI/CD automation |
| **Docker** | Containerization |
| **Python/FastAPI** | Example application |
| **Pytest** | Testing |

## 🚀 Pipeline Stages

Push → Test → Build Docker → Push to Registry → (Deploy)


## 🐳 Run with Docker

# Build image
docker build -t cicd-pipeline .

# Run container
docker run -d -p 8000:8000 cicd-pipeline

# Test
curl http://localhost:8000/health


📄 License

MIT
