# AGENTS.md

## Project overview

FitBuddy is a Python FastAPI app that generates personalized 7-day fitness plans, nutrition and recovery guidance, and AI-assisted plan updates. The main app entry is in [app/main.py](app/main.py), with routes in [app/routes.py](app/routes.py), settings in [app/config.py](app/config.py), database setup in [app/database.py](app/database.py), and AI logic under [app/ai](app/ai).

For project context and deeper design details, see:
- [README.md](README.md)
- [docs/05_development.md](docs/05_development.md)
- [docs/06_testing.md](docs/06_testing.md)
- [docs/03_design.md](docs/03_design.md)

## Working conventions

- Prefer the existing FastAPI + Pydantic pattern already used in the project.
- Keep route-level logic in [app/routes.py](app/routes.py) and business logic in [app/services](app/services) or the relevant AI module under [app/ai](app/ai).
- Use the centralized settings object from [app/config.py](app/config.py) for environment variables and avoid hardcoded secrets.
- Keep HTML templates in [templates](templates) and static assets in [static](static).
- Use the existing test patterns in [tests/test_app.py](tests/test_app.py) and [tests/conftest.py](tests/conftest.py) rather than inventing a new testing style.

## Environment and commands

Use the project venv for Python commands, or the equivalent local environment in the repo.

Typical setup:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

Run the app:

```bash
uvicorn app.main:app --reload
```

Run tests:

```bash
pytest -q
```

## Configuration

The app reads environment values from `.env` via the settings loader in [app/config.py](app/config.py). Important variables include:

- `GEMINI_API_KEY`
- `GEMINI_WORKOUT_MODEL`
- `GEMINI_TIP_MODEL`
- `MOCK_AI`
- `ADMIN_TOKEN`

Do not commit secrets, local `.env` files, SQLite DB files, or virtual environments.

## Repository-specific guidance

- The SQLite database is configured with a default path in [app/config.py](app/config.py). Changes should preserve the existing structure unless required by the feature.
- Existing tests are designed to validate the real HTTP behavior of the app and should remain the first line of verification for changes.
- The project documentation in [docs](docs) is intentionally phase-based. Prefer linking to those docs instead of duplicating them in agent instructions.
- The app is wellness software, not medical care; do not present AI-generated recommendations as diagnoses or prescriptions.
