
from pydantic import BaseModel, Field, validator


class Post(BaseModel):
    id: str
    title: str
    content: str
    author_id: str
    author: str
