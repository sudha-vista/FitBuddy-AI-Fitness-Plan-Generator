````markdown
# FitBuddy – AI Fitness Plan Generator

FitBuddy is an AI-powered web application that generates personalized 7-day workout plans based on user-provided fitness information, fitness goals, and workout intensity.

The application uses FastAPI for the backend, Jinja2 for the web interface, SQLite with SQLAlchemy for data storage, and Google Gemini for AI-generated workout and nutrition/recovery recommendations.

## Features

- Personalized 7-day workout plan generation
- Fitness-goal based workout recommendations
- Workout intensity selection
- AI-generated workout plans using Google Gemini
- General nutrition and recovery tips
- Feedback-based workout plan updates
- User and workout plan data storage
- SQLite database integration
- REST API endpoints
- User information retrieval
- Admin user management
- Input validation
- Safety-oriented AI prompts
- Automated testing using pytest
- Docker support
- Mock AI mode for development and testing

## Technologies Used

- Python
- FastAPI
- Jinja2
- SQLAlchemy
- SQLite
- Google Gemini API
- HTML
- CSS
- JavaScript
- Pytest
- Docker

## Project Structure

```text
FitBuddy-AI-Fitness-Plan-Generator/
│
├── 01-Brainstorming-and-Ideation/
├── 02-Requirement-Analysis/
├── 03-Project-Design/
├── 04-Project-Planning/
├── 05-Project-Development/
├── 06-Project-Testing/
├── 07-Project-Documentation/
├── 08-Project-Demonstration/
│
├── app/
├── templates/
├── tests/
│
├── .gitignore
├── AGENTS.md
├── Dockerfile
├── README.md
├── SUBMISSION_README.md
├── env.example
└── requirements.txt
````

## Project Phase Folders

### 01-Brainstorming-and-Ideation

Contains the brainstorming, problem identification, proposed solution, objectives, target users, and initial project ideas.

### 02-Requirement-Analysis

Contains the functional requirements, non-functional requirements, inputs, validation requirements, technical requirements, and feasibility information.

### 03-Project-Design

Contains the system design, application architecture, components, database entities, workflow, API design, and user interface design.

### 04-Project-Planning

Contains the project milestones, activities, execution plan, deliverables, and risk considerations.

### 05-Project-Development

Contains documentation related to the development and implementation of the FitBuddy application.

### 06-Project-Testing

Contains the testing approach, test cases, test environment, validation details, and testing information.

### 07-Project-Documentation

Contains the main project documentation, setup information, usage instructions, limitations, and future scope.

### 08-Project-Demonstration

Contains the demonstration procedure, recommended demonstration sequence, and evidence/checklist information.

## Application Folders

### app/

Contains the main FastAPI application source code, configuration, database setup, models, schemas, routes, AI modules, and application services.

### templates/

Contains the HTML templates used by the FitBuddy web application.

### tests/

Contains automated test files used to test application functionality.

## Root Files

### Dockerfile

Contains the configuration required to build and run the application using Docker.

### requirements.txt

Contains the Python dependencies required by the project.

### env.example

Provides an example of the environment variables required to configure the application.

### .gitignore

Specifies local files and directories that should not be committed to the Git repository.

### README.md

Provides project overview, setup, usage, API, testing, and other project information.

### SUBMISSION_README.md

Contains additional information prepared specifically for project submission.

### AGENTS.md

Contains project-related instructions and guidance included with the repository.

## Application Architecture

```text
User
  |
  v
Web Interface
  |
  v
FastAPI Application
  |
  +-- Routes
  |     |
  |     +-- Workout Plan Generation
  |     +-- User Information
  |     +-- Feedback
  |     +-- Admin Functions
  |
  +-- AI Modules
  |     |
  |     +-- Gemini Client
  |     +-- Workout Generator
  |     +-- Nutrition Generator
  |     +-- Plan Updater
  |
  +-- Database Layer
        |
        +-- SQLite / SQLAlchemy
```

## Main Application Components

### FastAPI Backend

FastAPI handles the application's web routes and API endpoints.

The backend is responsible for:

* Receiving user information
* Validating input
* Generating workout plans
* Handling feedback
* Managing user and plan information
* Providing API responses

### AI Components

The AI functionality is organized into separate modules.

**Gemini Client**

Handles communication with the configured Google Gemini model.

**Workout Generator**

Generates a personalized 7-day workout plan based on user information, goals, and intensity.

**Nutrition Generator**

Generates general nutrition and recovery tips.

**Plan Updater**

Uses user feedback to generate an updated workout plan.

## Database

FitBuddy uses SQLite for local data storage and SQLAlchemy for database interaction.

The project stores information related to:

* Users
* Workout plans
* User feedback and plan updates

The database is created locally when the application is initialized.

## Setup

### Prerequisites

Before running the project, make sure the following are installed:

* Python
* pip
* Git (if cloning the repository)
* Visual Studio Code or another Python-compatible IDE

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd FitBuddy-AI-Fitness-Plan-Generator
```

### 2. Create a Virtual Environment

For Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

For Windows Command Prompt:

```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a local `.env` file using `env.example` as a reference.

The environment configuration includes:

```text
GEMINI_API_KEY=
GEMINI_WORKOUT_MODEL=
GEMINI_TIP_MODEL=
MOCK_AI=
DATABASE_URL=
ADMIN_TOKEN=
```

Add your own Gemini API key to the local `.env` file when live Gemini generation is required.

**Do not upload the `.env` file or expose your API key in the GitHub repository.**

## Running the Application

Start the FastAPI development server using:

```bash
uvicorn app.main:app --reload
```

After the server starts, open:

```text
http://127.0.0.1:8000
```

The FastAPI interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

The application provides the following main API endpoints:

```text
GET    /api/health
POST   /api/plans
GET    /api/users/{user_id}
POST   /api/plans/{user_id}/feedback
GET    /api/users
DELETE /api/users/{user_id}
```

### Health Check

```text
GET /api/health
```

Used to check whether the application API is running.

### Generate Workout Plan

```text
POST /api/plans
```

Accepts user fitness information such as:

* Username
* User ID
* Age
* Weight
* Fitness goal
* Workout intensity

The application uses this information to generate the workout plan.

### Get User Information

```text
GET /api/users/{user_id}
```

Retrieves information associated with a particular user.

### Submit Feedback

```text
POST /api/plans/{user_id}/feedback
```

Allows feedback to be submitted for an existing workout plan.

The feedback can be used by the application to generate an updated plan.

### Admin User Endpoints

```text
GET /api/users
DELETE /api/users/{user_id}
```

These endpoints are intended for administrative user management and require the configured admin authorization.

## Example Input

An example workout-plan request can contain information such as:

```json
{
  "username": "Alex",
  "user_id": "alex01",
  "age": 24,
  "weight": 68,
  "goal": "muscle gain",
  "intensity": "medium"
}
```

The application uses the submitted information to generate a personalized workout plan.

## AI Model Configuration

The project uses Google Gemini through a configurable AI client.

The workout and nutrition/recovery generation models are configured through environment variables rather than being fixed in this README.

This allows the configured model to be changed without changing the main application code.

The project also includes a mock-AI option for development and testing.

## Mock AI Mode

The application can be configured to use mock AI responses during development and testing.

This is useful when:

* A Gemini API key is not available
* Live API calls are not required
* Automated tests are being executed
* Development is being performed without external AI requests

The setting is controlled through the environment configuration.

```text
MOCK_AI=true
```

## Testing

The project contains automated tests using pytest.

To run the test suite:

```bash
pytest -q
```

The tests are designed to verify important application functionality and API behavior.

Testing should be performed after installing the project dependencies and configuring the required environment settings.

## Safety and Responsible Use

FitBuddy is intended for general fitness planning and educational purposes.

The application does not provide medical diagnosis or medical treatment.

The generated workout and nutrition information should be treated as general guidance rather than professional medical advice.

Users should consider their individual circumstances and consult a qualified healthcare professional when appropriate.

The application is designed to avoid generating medical diagnosis or treatment recommendations.

## Docker

A Dockerfile is included in the repository for containerized deployment.

To build the Docker image:

```bash
docker build -t fitbuddy .
```

The container should be provided with the required environment configuration when it is run.

## Development

The project is organized into separate modules to make the application easier to maintain and test.

The main application functionality is contained within the `app` folder.

The project separates:

* Configuration
* Database handling
* Data models
* API routes
* AI functionality
* Workout generation
* Nutrition/recovery generation
* Feedback-based plan updates

This modular organization allows individual parts of the application to be developed and tested separately.

## Project Workflow

The basic workflow of FitBuddy is:

```text
1. User enters fitness information
           |
           v
2. Application validates the input
           |
           v
3. User's fitness goal and intensity are processed
           |
           v
4. Gemini generates a personalized workout plan
           |
           v
5. Application stores the plan and user information
           |
           v
6. User views the generated plan
           |
           v
7. User can provide feedback
           |
           v
8. Application can generate an updated plan
```

## Project Documentation

The repository contains documentation for all eight project phases:

1. Brainstorming and Ideation
2. Requirement Analysis
3. Project Design
4. Project Planning
5. Project Development
6. Project Testing
7. Project Documentation
8. Project Demonstration

These documents describe the project from initial idea through development, testing, documentation, and demonstration.

## Limitations

* AI-generated recommendations may not be suitable for every individual.
* The application is intended for general fitness guidance.
* Live Gemini functionality requires a valid API configuration.
* The application uses a local SQLite database by default.
* The quality of generated plans depends on the information provided by the user and the configured AI model.

## Future Scope

Possible future improvements include:

* User authentication
* More detailed progress tracking
* Workout history
* Additional fitness goals
* More exercise customization
* Improved user interface
* Cloud database integration
* Deployment to a cloud platform
* Additional AI-powered fitness features

## Conclusion

FitBuddy is an AI-powered fitness planning application that combines FastAPI, Google Gemini, SQLite, SQLAlchemy, and a web-based interface.

The application demonstrates how AI can be integrated into a web application to generate personalized workout plans, provide general nutrition and recovery tips, process user feedback, and maintain user and plan information.

The project also includes separate documentation for brainstorming, requirements, design, planning, development, testing, documentation, and demonstration.

```

**Use this as `README.md`.** Your `SUBMISSION_README.md` remains a separate file; you don't need to merge the two.
```

