# Phase 7 – Project Documentation

**Project:** FitBuddy – AI Fitness Plan Generator

## 1. Project Overview

FitBuddy is an AI-assisted web application for generating personalized seven-day workout plans, nutrition/recovery tips and feedback-based plan revisions.

## 2. Technologies Used

Python, FastAPI, Pydantic, Jinja2, SQLAlchemy, SQLite, Google GenAI SDK, HTML, CSS, JavaScript, Uvicorn and pytest.

## 3. Core Features

User input form; AI-generated seven-day workout plan; nutrition/recovery tip; feedback-based revised plan; persistent user/plan storage; admin view; REST API; Swagger/OpenAPI documentation.

## 4. Installation and Setup

Create a Python virtual environment, install requirements.txt, create .env from .env.example, configure GEMINI_API_KEY for live AI use or set MOCK_AI=true for test mode, then run Uvicorn.

## 5. Usage Flow

Open the home page → enter details → generate plan → review plan/tip → submit optional feedback → review updated plan → optionally review stored users through the admin view.

## 6. Limitations and Responsible Use

FitBuddy is presented in the code as a general wellness tool, not medical care. The AI prompts explicitly avoid diagnosis and treatment. The application should not be treated as a substitute for professional medical advice. Production deployment would need stronger authentication/authorization and other production safeguards.

## 7. Conclusion

The project demonstrates integration of a web framework, database persistence, generative AI, frontend templates, REST APIs and automated testing in one modular application.

## 8. Future Scope

Possible future work includes stronger authentication, richer user progress tracking, improved production deployment, expanded test coverage, additional personalization controls and more robust monitoring.
