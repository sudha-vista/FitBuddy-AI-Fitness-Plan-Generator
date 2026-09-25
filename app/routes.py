from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.orm import Session
from .database import get_db
from .dependencies import require_admin
from .schemas import FeedbackRequest, PlanResponse, UserInput, UserSummary
from .services.plan_service import create_plan, delete_user, get_user_or_404, update_plan

templates = Jinja2Templates(directory="templates")
router = APIRouter()
api = APIRouter(prefix="/api")

def _context(user, message=None):
    p = user.plan
    return {"username": user.username, "user_id": user.user_id, "age": user.age, "weight": user.weight,
            "goal": user.goal, "intensity": user.intensity, "workout_plan": p.original_plan,
            "updated_plan": p.updated_plan, "nutrition_tip": p.nutrition_tip, "feedback": p.feedback,
            "message": message, "error": None}

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"error": None})

@router.post("/generate-workout", response_class=HTMLResponse)
def generate_workout_form(request: Request, username: str = Form(...), user_id: str = Form(...),
                          age: int = Form(...), weight: float = Form(...), goal: str = Form(...),
                          intensity: str = Form(...), db: Session = Depends(get_db)):
    try:
        data = UserInput(username=username.strip(), user_id=user_id.strip(), age=age, weight=weight, goal=goal, intensity=intensity)
        user, _ = create_plan(db, data)
        return templates.TemplateResponse(request=request, name="result.html", context=_context(user))
    except Exception as exc:
        return templates.TemplateResponse(request=request, name="index.html",
                                          context={"error": getattr(exc, "detail", str(exc))}, status_code=400)

@router.post("/submit-feedback", response_class=HTMLResponse)
def submit_feedback_form(request: Request, user_id: str = Form(...), feedback: str = Form(...),
                         db: Session = Depends(get_db)):
    try:
        user = get_user_or_404(db, user_id.strip())
        body = FeedbackRequest(feedback=feedback.strip())
        update_plan(db, user, body.feedback)
        user = get_user_or_404(db, user_id.strip())
        return templates.TemplateResponse(request=request, name="result.html",
                                          context=_context(user, "Your plan was updated successfully."))
    except Exception as exc:
        return templates.TemplateResponse(request=request, name="result.html",
            context={"error": getattr(exc, "detail", str(exc)), "message": None, "user_id": user_id,
                     "workout_plan": "", "updated_plan": None, "nutrition_tip": ""}, status_code=400)

@router.get("/view-all-users", response_class=HTMLResponse, dependencies=[Depends(require_admin)])
def view_all_users(request: Request, db: Session = Depends(get_db)):
    from .models import User
    users = db.scalars(select(User).order_by(User.created_at.desc())).all()
    return templates.TemplateResponse(request=request, name="all_users.html", context={"users": users})

@api.get("/health")
def health():
    return {"status": "ok", "service": "FitBuddy"}

@api.post("/plans", response_model=PlanResponse, status_code=201)
def api_create_plan(data: UserInput, db: Session = Depends(get_db)):
    user, plan = create_plan(db, data)
    return PlanResponse(user_id=user.user_id, username=user.username, goal=user.goal, intensity=user.intensity,
                        workout_plan=plan.original_plan, nutrition_tip=plan.nutrition_tip)

@api.get("/users", response_model=list[UserSummary], dependencies=[Depends(require_admin)])
def api_list_users(db: Session = Depends(get_db)):
    from .models import User
    users = db.scalars(select(User).order_by(User.created_at.desc())).all()
    return [UserSummary(user_id=u.user_id, username=u.username, age=u.age, weight=u.weight,
                        goal=u.goal, intensity=u.intensity, has_updated_plan=bool(u.plan and u.plan.updated_plan))
            for u in users]

@api.get("/users/{user_id}", response_model=PlanResponse)
def api_get_user(user_id: str, db: Session = Depends(get_db)):
    user = get_user_or_404(db, user_id)
    p = user.plan
    return PlanResponse(user_id=user.user_id, username=user.username, goal=user.goal, intensity=user.intensity,
                        workout_plan=p.original_plan, nutrition_tip=p.nutrition_tip,
                        updated_plan=p.updated_plan, feedback=p.feedback)

@api.post("/plans/{user_id}/feedback", response_model=PlanResponse)
def api_update_plan(user_id: str, data: FeedbackRequest, db: Session = Depends(get_db)):
    user = get_user_or_404(db, user_id)
    p = update_plan(db, user, data.feedback)
    return PlanResponse(user_id=user.user_id, username=user.username, goal=user.goal, intensity=user.intensity,
                        workout_plan=p.original_plan, nutrition_tip=p.nutrition_tip,
                        updated_plan=p.updated_plan, feedback=p.feedback)

@api.delete("/users/{user_id}", status_code=204, dependencies=[Depends(require_admin)])
def api_delete_user(user_id: str, db: Session = Depends(get_db)):
    delete_user(db, user_id)
