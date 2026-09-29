from datetime import datetime, timezone
from sqlalchemy import select
from fastapi import HTTPException
from ..models import Plan, User
from ..ai.workout_generator import generate_workout_gemini
from ..ai.nutrition_generator import generate_nutrition_tip_with_flash
from ..ai.plan_updater import update_workout_plan

def create_plan(db, data):
    if db.scalar(select(User).where(User.user_id == data.user_id)):
        raise HTTPException(status_code=409, detail="User ID already exists.")
    workout = generate_workout_gemini(data.username, data.age, data.weight, data.goal, data.intensity)
    tip = generate_nutrition_tip_with_flash(data.goal)
    user = User(user_id=data.user_id, username=data.username, age=data.age, weight=data.weight, goal=data.goal, intensity=data.intensity)
    user.plan = Plan(original_plan=workout, nutrition_tip=tip)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user, user.plan

def get_user(db, user_id):
    return db.scalar(select(User).where(User.user_id == user_id))

def get_user_or_404(db, user_id):
    user = get_user(db, user_id)
    if not user or not user.plan:
        raise HTTPException(status_code=404, detail="User or workout plan not found.")
    return user

def update_plan(db, user, feedback):
    base_plan = user.plan.updated_plan or user.plan.original_plan
    revised = update_workout_plan(base_plan, feedback, user.goal, user.intensity)
    user.plan.updated_plan = revised
    user.plan.feedback = feedback
    user.plan.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(user.plan)
    return user.plan

def delete_user(db, user_id):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    db.delete(user)
    db.commit()
