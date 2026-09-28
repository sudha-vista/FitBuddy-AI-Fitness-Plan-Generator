# FitBuddy – AI Fitness Plan Generator

FastAPI + Jinja2 + SQLite/SQLAlchemy + Google Gemini application for personalized 7-day workout plans, nutrition/recovery tips, feedback-based plan updates, and an admin view.

## Structure

```text
FitBuddy/
├── app/
│   ├── main.py config.py database.py models.py schemas.py dependencies.py routes.py
│   ├── ai/
│   │   ├── gemini_client.py workout_generator.py nutrition_generator.py plan_updater.py
│   └── services/plan_service.py
├── templates/{base,index,result,all_users}.html
├── static/css/style.css
├── static/js/app.js
├── tests/{conftest,test_app}.py
├── docs/01_brainstorming.md ... 08_demonstration.md
├── .env.example .gitignore requirements.txt Dockerfile README.md
```

## Setup in VS Code

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

Command Prompt:

```cmd
python -m venv .venv
.venv\Scriptsctivate
pip install --upgrade pip
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and set:

```env
GEMINI_API_KEY=your_key
```

For testing without a key:

```env
MOCK_AI=true
```

## Run

```bash
uvicorn app.main:app --reload
```

Open:
- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/view-all-users

## Test

```bash
pytest -q
```

## API

`GET /api/health`

`POST /api/plans`

```json
{
  "username": "Alex",
  "user_id": "alex001",
  "age": 24,
  "weight": 68,
  "goal": "muscle gain",
  "intensity": "medium"
}
```

`GET /api/users/{user_id}`

`POST /api/plans/{user_id}/feedback`

```json
{"feedback":"Add more cardio and one extra rest day."}
```

`GET /api/users`

`DELETE /api/users/{user_id}`

## Gemini model note

The supplied document specifies Gemini 1.5 Pro and Gemini Flash. Those model references are legacy now, so the project uses configurable current model IDs:

```env
GEMINI_WORKOUT_MODEL=gemini-2.5-pro
GEMINI_TIP_MODEL=gemini-3.8-flash
```

If your API account does not have access to the workout model, set `GEMINI_WORKOUT_MODEL` to an available current Gemini model.

## Safety

FitBuddy is general wellness software, not medical care. AI output is not a diagnosis or prescription.

Do not commit `.env`, API keys, `fitbuddy.db`, or `.venv`.

The `docs/` folder contains the eight phase-wise documents requested by the supplied project instructions.
