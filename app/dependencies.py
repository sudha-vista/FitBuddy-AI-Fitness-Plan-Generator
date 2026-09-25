from fastapi import Header, HTTPException
from .config import get_settings

def require_admin(x_admin_token: str | None = Header(default=None)):
    token = get_settings().admin_token
    if token and x_admin_token != token:
        raise HTTPException(status_code=401, detail="Invalid or missing admin token.")
