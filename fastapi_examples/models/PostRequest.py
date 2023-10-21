
from pydantic import BaseModel


class PostRequest(BaseModel):
    user_name: str
    title: str
    content: str
