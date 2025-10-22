
from urllib.parse import urlencode

def start_auth_url(state: str):
    base_url = "https://accounts.google.com/o/oauth2/v2/auth"
    params = {
        "client_id": "YOUR_CLIENT_ID",
        "redirect_uri": "http://localhost:8000/api/callback",
        "response_type": "code",
        "scope": "https://www.googleapis.com/auth/youtube.readonly",
        "access_type": "offline",
        "state": state,
        "prompt": "consent"
    }
    return f"{base_url}?{urlencode(params)}"
