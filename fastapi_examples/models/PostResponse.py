
from pydantic import BaseModel, Field, validator
from fastapi_examples.models.Post import Post
from typing import List


class PostResponse(BaseModel):
    success: bool = True
    message: str
    data: List[Post]

