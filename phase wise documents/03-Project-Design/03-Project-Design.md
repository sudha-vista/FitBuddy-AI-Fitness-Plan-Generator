# Phase 3 – Project Design

**Project:** FitBuddy – AI Fitness Plan Generator

## 1. High-Level Architecture

Browser/UI → FastAPI routes → Service layer → AI generation and SQLite database → Response rendered through Jinja2 templates.

## 2. Major Components

Frontend: Jinja2 templates, CSS and JavaScript.
Backend: FastAPI routes and Pydantic schemas.
Service layer: plan creation, retrieval and update logic.
AI layer: Gemini client, workout generator, nutrition generator and plan updater.
Database layer: SQLAlchemy models and SQLite.
Testing layer: pytest and FastAPI TestClient.

## 3. Main Data Entities

User: database ID, user ID, username, age, weight, goal, intensity and creation time.
Plan: plan ID, linked user, original plan, updated plan, nutrition tip, feedback, update time and creation time.

## 4. Main Workflow

1. User opens the home page.
2. User enters profile and fitness details.
3. FastAPI validates the request.
4. Service layer calls the workout and nutrition generators.
5. The result is stored in SQLite.
6. The result page displays the original plan and tip.
7. User may submit feedback.
8. The updater creates a revised plan and stores it separately.
9. Admin view can display stored users and their plans.

## 5. API Design

GET /api/health – service health check.
POST /api/plans – create a plan.
GET /api/users/{user_id} – retrieve a user plan.
POST /api/plans/{user_id}/feedback – update a plan from feedback.
GET /api/users – list users for the admin context.
DELETE /api/users/{user_id} – delete a user.

## 6. UI Pages

Home/Create Plan page; Personalized Plan/Result page; Admin Dashboard; FastAPI /docs page.

## 7. Design Note

The project uses a modular architecture so UI, routes, business logic, AI integration and persistence are separated rather than being placed in one file.
