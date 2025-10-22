# backend/app/oauth_helpers.py
import secrets, time
state_store = {}
def make_state():
    s = secrets.token_urlsafe(16)
    state_store[s] = {"created_at": time.time()}
    return s
def validate_state(s):
    if s not in state_store:
        raise Exception("Invalid state")
    return True
