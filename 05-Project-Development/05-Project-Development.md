# Phase 5 – Project Development

**Project:** FitBuddy – AI Fitness Plan Generator

## 1. Development Environment

The repository is structured as a Python FastAPI application. It includes requirements.txt, environment configuration, application modules, templates, static assets and tests.

## 2. Backend Development

main.py creates the FastAPI application and mounts static assets. routes.py defines HTML and REST routes. schemas.py defines validated request/response models. services/plan_service.py contains plan creation and update logic.

## 3. Database Development

models.py defines User and Plan SQLAlchemy models with a one-to-one relationship. database.py creates the SQLAlchemy engine/session and initializes database tables.

## 4. AI Integration

gemini_client.py creates a Google GenAI client when a real AI call is required. workout_generator.py generates a seven-day workout plan. nutrition_generator.py generates a general nutrition/recovery tip. plan_updater.py creates a revised plan from user feedback. MOCK_AI is available for testing without consuming AI quota.

## 5. Frontend Development

The project contains Jinja2 templates for the base layout, input form, result page and admin dashboard. CSS provides responsive styling and JavaScript disables the submit button while generation is in progress.

## 6. Configuration and Deployment

The application reads configuration from .env. The documented local run command is uvicorn app.main:app --reload. The project also includes a Dockerfile.

## 7. Existing Project Evidence

The supplied project archive contains the implemented application code, templates, static files, tests, requirements.txt, Dockerfile, README and eight phase markdown files.
