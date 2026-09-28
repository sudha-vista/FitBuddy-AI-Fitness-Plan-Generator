from functools import lru_cache
from ..config import get_settings


class GeminiServiceError(RuntimeError):
    """Raised when Gemini cannot be called successfully."""


@lru_cache
def get_client():
    """Create the Gemini client only when a real AI call is needed."""
    settings = get_settings()
    if not settings.gemini_api_key:
        raise GeminiServiceError(
            "GEMINI_API_KEY is not configured. Set it in .env or enable MOCK_AI=true."
        )

    # Lazy import lets MOCK_AI=true tests run even if the Gemini package is absent.
    try:
        from google import genai
    except ImportError as exc:
        raise GeminiServiceError(
            "google-genai is not installed. Run: pip install -r requirements.txt"
        ) from exc

    return genai.Client(api_key=settings.gemini_api_key)


def generate_text(prompt: str, model: str) -> str:
    try:
        response = get_client().models.generate_content(
            model=model,
            contents=prompt,
        )
        text = getattr(response, "text", None)
        if not text:
            raise GeminiServiceError("Gemini returned an empty response.")
        return text.strip()
    except GeminiServiceError:
        raise
    except Exception as exc:
        raise GeminiServiceError(f"Gemini request failed: {exc}") from exc
