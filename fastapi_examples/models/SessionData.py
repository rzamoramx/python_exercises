
from pydantic import BaseModel


class SessionData(BaseModel):
    username: str
    last_activity: str = None
