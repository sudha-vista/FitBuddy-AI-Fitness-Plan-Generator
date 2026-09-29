from .gemini_client import generate_text
from ..config import get_settings

def _mock_tip(goal):
    tips = {
        "weight loss": "Build meals around vegetables, a protein source, whole foods, and appropriate portions. Stay hydrated.",
        "muscle gain": "Include a protein-rich food in regular meals and combine it with enough overall energy and carbohydrates to support training.",
        "general wellness": "Prioritize regular meals, vegetables and fruit, protein-rich foods, whole grains, hydration, and adequate sleep.",
        "flexibility": "Stay hydrated and include balanced meals with enough protein and micronutrient-rich foods to support recovery.",
    }
    return tips.get(goal, tips["general wellness"])

def generate_nutrition_tip_with_flash(goal):
    settings = get_settings()
    if settings.mock_ai:
        return _mock_tip(goal)
    prompt = f"""
You are FitBuddy's nutrition and recovery tip component.
Fitness goal: {goal}
Return one concise, practical nutrition or recovery tip in 2–4 sentences.
Keep it general wellness guidance, not individualized medical treatment.
Avoid exact calorie prescriptions or supplement dosing.
"""
    return generate_text(prompt, settings.gemini_tip_model)
