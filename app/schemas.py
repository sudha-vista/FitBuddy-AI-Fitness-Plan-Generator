from typing import Literal
from pydantic import BaseModel, Field, ConfigDict

Goal = Literal["weight loss", "muscle gain", "general wellness", "flexibility"]
Intensity = Literal["low", "medium", "high"]

class UserInput(BaseModel):
    username: str = Field(min_length=2, max_length=120)
    user_id: str = Field(min_length=2, max_length=80, pattern=r"^[A-Za-z0-9_-]+$")
    age: int = Field(ge=13, le=100)
    weight: float = Field(gt=20, le=500)
    goal: Goal
    intensity: Intensity

class FeedbackRequest(BaseModel):
    feedback: str = Field(min_length=3, max_length=1000)

class PlanResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: str
    username: str
    goal: str
    intensity: str
    workout_plan: str
    nutrition_tip: str
    updated_plan: str | None = None
    feedback: str | None = None

class UserSummary(BaseModel):
    user_id: str
    username: str
    age: int
    weight: float
    goal: str
    intensity: str
    has_updated_plan: bool
