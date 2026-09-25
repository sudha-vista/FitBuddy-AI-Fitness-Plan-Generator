# Phase 2 – Requirement Analysis

**Project:** FitBuddy – AI Fitness Plan Generator

## 1. Functional Requirements

FR1 – Collect username, user ID, age, weight, goal and intensity.
FR2 – Validate input using Pydantic constraints.
FR3 – Generate a seven-day workout plan.
FR4 – Generate a nutrition/recovery tip.
FR5 – Store users and plans in SQLite through SQLAlchemy.
FR6 – Preserve the original plan when feedback is submitted.
FR7 – Generate/store an updated plan and feedback.
FR8 – Provide an admin view of registered users and plans.
FR9 – Provide REST endpoints for plan creation, retrieval, update and user listing.
FR10 – Provide a health endpoint and FastAPI interactive documentation.

## 2. Non-Functional Requirements

• Responsive browser interface.
• Modular Python application structure.
• Environment-based configuration and API-key handling.
• Persistent local database storage.
• Automated tests for core workflows.
• Local deployment through Uvicorn.

## 3. Input Requirements

Name; user ID; age; weight in kg; fitness goal; workout intensity; optional feedback for plan revision.

## 4. Validation Requirements

Username length: 2–120 characters. User ID length: 2–80 characters and restricted to letters, numbers, underscore and hyphen. Age: 13–100. Weight: greater than 20 kg and at most 500 kg. Goal: weight loss, muscle gain, general wellness, or flexibility. Intensity: low, medium, or high. Feedback: 3–1000 characters.

## 5. Software/Technology Requirements

Python; FastAPI; Pydantic; Jinja2; SQLAlchemy; SQLite; Google GenAI SDK; HTML/CSS/JavaScript; Uvicorn; pytest.

## 6. Security/Configuration Requirements

The Gemini API key is intended to be stored in a .env file and not committed to version control. The project includes an admin-token mechanism for the admin view/API. Production deployment would require stronger authentication and authorization.

## 7. Feasibility

Technical feasibility is supported by the modular FastAPI structure, SQLite persistence, configurable AI client, and automated tests included in the project. Operational feasibility depends on having Python dependencies and, for real AI generation, a valid Gemini API configuration.
