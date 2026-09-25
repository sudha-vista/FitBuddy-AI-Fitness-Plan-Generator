````markdown
# FitBuddy – AI Fitness Plan Generator

FitBuddy is a web-based AI fitness plan generator that creates personalized 7-day workout plans based on user-provided fitness goals and preferences. The application also provides general nutrition/recovery tips and allows users to submit feedback for plan updates.

## Technologies Used

- Python
- FastAPI
- Jinja2
- SQLite
- SQLAlchemy
- Google Gemini
- HTML
- CSS
- JavaScript

## Project Structure

FitBuddy/
├── 01-Brainstorming-and-Ideation/
├── 02-Requirement-Analysis/
├── 03-Project-Design/
├── 04-Project-Planning/
├── 05-Project-Development/
├── 06-Project-Testing/
├── 07-Project-Documentation/
├── 08-Project-Demonstration/
├── app/
├── templates/
├── tests/
├── .gitignore
├── AGENTS.md
├── Dockerfile
├── README.md
├── SUBMISSION_README.md
├── env.example
└── requirements.txt

## Setup

Create and activate a Python virtual environment, then install the required dependencies.

```bash
python -m venv .venv
````

Windows PowerShell:

```bash
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file based on `env.example` and add the required configuration values.

Do not upload the `.env` file or expose API keys in the repository.

## Run the Application

Start the FastAPI application using:

```bash
uvicorn app.main:app --reload
```

Open the application at:

```text
http://127.0.0.1:8000
```

The API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

The admin users page is available at:

```text
http://127.0.0.1:8000/view-all-users
```

## Main Features

* User fitness information input
* AI-generated 7-day workout plan
* General nutrition and recovery tips
* Feedback-based workout plan updates
* SQLite database storage
* FastAPI backend
* Web-based interface
* API endpoints for plan and user operations
* Admin view for user information

## Testing

The project contains automated tests in the `tests/` folder.

Run the tests using:

```bash
pytest -q
```

Testing details and test documentation are available in:

```text
06-Project-Testing/
```

## Project Documentation

The project is organized into eight project phases:

1. Brainstorming and Ideation
2. Requirement Analysis
3. Project Design
4. Project Planning
5. Project Development
6. Project Testing
7. Project Documentation
8. Project Demonstration

The corresponding documents are available in the numbered project folders.

## Project Demonstration

The demonstration phase explains the recommended sequence for presenting the application, including the user input, workout-plan generation, feedback process, and relevant project evidence.

The demonstration documentation is available in:

```text
08-Project-Demonstration/
```

## Responsible Use

FitBuddy provides general fitness and wellness information. It is not intended to diagnose medical conditions or provide medical treatment.

Users should seek appropriate professional advice for medical or health-related concerns.

## Future Scope

Possible future improvements include:

* Improved user interface
* Additional personalization options
* More detailed progress tracking
* Additional AI-generated fitness features
* Deployment to a cloud environment


