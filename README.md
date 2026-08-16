# 🚀 CICD Pipeline App

A production-ready FastAPI application demonstrating modern DevOps practices including containerization, continuous integration, and continuous deployment.

[![Test Pipeline](https://github.com/Zetta-kun/cicd-pipeline/actions/workflows/test.yml/badge.svg)](https://github.com/Zetta-kun/cicd-pipeline/actions/workflows/test.yml)
[![Build & Deploy](https://github.com/Zetta-kun/cicd-pipeline/actions/workflows/build-deploy.yml/badge.svg)](https://github.com/Zetta-kun/cicd-pipeline/actions/workflows/build-deploy.yml)
[![Python Versions](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docker Pulls](https://img.shields.io/badge/docker-ghcr.io-blue.svg)](https://github.com/Zetta-kun/cicd-pipeline/pkgs/container/YOUR_REPO)

---

## 📋 Table of Contents

- [About The Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)

---

## 📖 About The Project

**CICD Pipeline App** is a FastAPI-based REST API that serves as a comprehensive example of modern DevOps practices. This project demonstrates how to build, test, containerize, and deploy a Python application using industry-standard tools and practices.

### Why This Project?

- 🎯 **Production-ready** - Built with best practices in mind
- 🔒 **Secure** - Non-root user, minimal Docker images
- 🚀 **Automated** - Full CI/CD pipeline with GitHub Actions
- 📦 **Containerized** - Multi-stage Docker builds with caching
- 🧪 **Tested** - Unit tests with coverage reporting
- 📊 **Monitored** - Health check endpoints for monitoring

---

## ✨ Features

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Welcome message and API information |
| `/datetime` | GET | Current date and time (with Redis caching) |
| `/health` | GET | Health check for load balancers and monitoring |
| `/version` | GET | Application version and environment info |
| `/stats` | GET | System statistics and cache information |
| `/docs` | GET | Interactive API documentation (Swagger UI) |
| `/redoc` | GET | Alternative API documentation (ReDoc) |

### DevOps Features

- ✅ **Multi-stage Dockerfile** - Optimized image size (~120MB vs ~180MB)
- ✅ **Multi-arch support** - Builds for both amd64 and arm64
- ✅ **Redis caching** - Reduces API response time
- ✅ **Health checks** - Docker HEALTHCHECK and `/health` endpoint
- ✅ **Non-root user** - Container runs as non-privileged user
- ✅ **Hot reload** - Development mode with `--reload`
- ✅ **CI/CD pipeline** - Automated testing, building, and deployment
- ✅ **Test matrix** - Tests against Python 3.10, 3.11, 3.12
- ✅ **Code coverage** - Enforces minimum 70% coverage
- ✅ **Semver tagging** - Automatic version tagging

---

## 🛠️ Tech Stack

### Backend
- **FastAPI** (0.109.0) - Modern Python web framework
- **Uvicorn** (0.27.0) - ASGI server
- **Pydantic** (2.5.3) - Data validation
- **Redis** (5.0.1) - Caching layer

### DevOps & Infrastructure
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **GitHub Actions** - CI/CD pipeline
- **GitHub Container Registry (GHCR)** - Docker image registry

### Testing & Quality
- **pytest** (7.4.4) - Testing framework
- **pytest-cov** (4.1.0) - Code coverage
- **flake8** (7.0.0) - Code linting
- **Black** (24.1.1) - Code formatting

---

## 🏗️ Architecture

┌─────────────────────────────────────────────────────────────┐
│ GitHub Actions │
│ ┌──────────────┐ ┌──────────────────────────────┐ │
│ │ Test Job │───────▶│ Build & Push Job │ │
│ │ │ │ │ │
│ │ - Lint │ │ - Build multi-arch image │ │
│ │ - Test 3.10 │ │ - Push to GHCR │ │
│ │ - Test 3.11 │ │ - Tag with semver │ │
│ │ - Test 3.12 │ │ - Cache layers │ │
│ └──────────────┘ └──────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────┐
│ Docker Compose Stack │
│ ┌─────────────┐ ┌─────────────────────────────┐ │
│ │ API │◀───────▶│ Redis │ │
│ │ FastAPI │ │ (Cache Service) │ │
│ │ :8000 │ │ :6379 │ │
│ └─────────────┘ └─────────────────────────────┘ │
│ │ │
│ │ Health Check │
│ ▼ │
│ /health endpoint │
└─────────────────────────────────────────────────────────────┘


