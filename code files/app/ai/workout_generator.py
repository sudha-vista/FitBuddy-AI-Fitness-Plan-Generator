from .gemini_client import generate_text
from ..config import get_settings

def _mock_workout(username, goal, intensity, age, weight):
    return (
        "7-DAY FITBUDDY WORKOUT PLAN\n\n"
        f"User: {username}\nAge: {age}\nWeight: {weight:.1f} kg\nGoal: {goal}\nIntensity: {intensity}\n\n"
        "Day 1 – Full Body Foundation\nWarm-up: 5–10 minutes. Main: Squats 3x10, incline push-ups 3x8, glute bridges 3x12, plank 3x20–30 sec. Cooldown: 5 minutes.\n\n"
        "Day 2 – Cardio & Core\nWarm-up: 5 minutes. Main: Brisk walk/cycle 20–30 minutes, dead bug 3x10/side, bird dog 3x10/side. Cooldown: easy walking.\n\n"
        "Day 3 – Recovery & Mobility\nEasy walk 15–20 minutes plus 10–15 minutes comfortable mobility.\n\n"
        "Day 4 – Lower Body\nWarm-up: 5–10 minutes. Main: Squats 3x10, reverse lunges 3x8/side, calf raises 3x15, glute bridges 3x12. Cooldown: 5–10 minutes.\n\n"
        "Day 5 – Upper Body & Core\nWarm-up: 5–10 minutes. Main: Incline push-ups 3x8, band rows 3x12, shoulder raises 2x12, plank 3x20–30 sec. Cooldown: gentle stretching.\n\n"
        "Day 6 – Light Cardio & Flexibility\n20–30 minutes comfortable cardio followed by 10 minutes stretching.\n\n"
        "Day 7 – Rest\nRest, hydration, sleep, and gentle walking if desired.\n\n"
        "Safety note: Adjust exercises to your experience and equipment. Stop if an exercise causes pain and seek professional advice when appropriate."
    )

def generate_workout_gemini(username, age, weight, goal, intensity):
    settings = get_settings()
    if settings.mock_ai:
        return _mock_workout(username, goal, intensity, age, weight)
    prompt = f"""
You are the workout-planning component of FitBuddy, an educational wellness application.
Create a structured 7-day workout plan for:
Name: {username}
Age: {age}
Weight: {weight} kg
Goal: {goal}
Preferred intensity: {intensity}
Requirements:
- Exactly 7 days.
- Include training and recovery.
- Each day: focus, warm-up, exercises with sets/reps or duration, rest guidance, cooldown/recovery.
- Practical for a general user.
- Do not diagnose conditions or prescribe treatment.
- Do not claim guaranteed health or body-composition outcomes.
- Include a short safety note.
- Plain text with clear headings; no JSON or tables.
"""
    return generate_text(prompt, settings.gemini_workout_model)
