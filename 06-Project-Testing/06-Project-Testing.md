# Phase 6 – Project Testing

**Project:** FitBuddy – AI Fitness Plan Generator

## 1. Testing Approach

The project includes automated tests using pytest and FastAPI TestClient. The test configuration enables MOCK_AI and a separate SQLite test database.

## 2. Test Cases

TC01 – Home page: expected HTTP 200 and FitBuddy text; included in test_home.
TC02 – Health API: expected HTTP 200 and status=ok; included in test_health.
TC03 – Create/get/update plan: create returns 201, generated plan contains Day 1, retrieval succeeds, feedback produces an updated plan.
TC04 – Duplicate ID: second creation with the same user ID returns HTTP 409.
TC05 – HTML form: submitting valid form data returns HTTP 200 and displays Original 7-Day Workout Plan.

## 3. Test Environment

pytest; FastAPI TestClient; MOCK_AI=true; SQLite test database.

## 4. Expected Test Command

pytest -q

## 5. Result Recording

Before submission, run the test command and record the actual terminal result in this document or attach a screenshot. Do not claim a test passed unless it has been executed.

## 6. Additional Manual Tests

Test invalid age/weight, invalid goal/intensity, missing required fields, feedback submission, admin view, /docs page, API-key configuration, and application startup.

## 7. Testing Limitation

The automated tests use mock AI responses. They verify application flow without requiring live Gemini generation. A separate manual check is needed for live Gemini API integration.
