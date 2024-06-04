
import structlog
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from intermediate_topics.sql.sqlalchemy.repositories.PostRepository import PostRepository
from intermediate_topics.sql.sqlalchemy.repositories.UserRepository import UserRepository
from fastapi_examples.models.PostResponse import PostResponse
from fastapi_examples.models.PostRequest import PostRequest
from fastapi_examples.models.UserRequest import UserRequest
from intermediate_topics.sql.sqlalchemy.models.Post import Post
from intermediate_topics.sql.sqlalchemy.models.User import User
from fastapi_examples.security.session_manager import session_cookie, SessionData, session_manager, session_verifier


router = APIRouter()
LOG = structlog.get_logger("blog_v1")


@router.post("/user")
async def create_user(user_req: UserRequest):
    LOG.info("create_user", user=user_req)
    user_repo = UserRepository()

    user = User()
    user.username = user_req.username
    user.email = user_req.email
    user.password = user_req.password

    user_repo.save(user)

    return "user created"


@router.post("/post")
async def create_post(post_request: PostRequest, session_id: UUID = Depends(session_cookie)):
    session = await session_manager.read(session_id)

    LOG.info("create_post", user_name=post_request.user_name)
    LOG.info("session_data.username", session_data_username=session.username)
    session.last_activity = "post created"
    session_manager.update(session_id, session)

    user_repo = UserRepository()
    post_repo = PostRepository()

    user = user_repo.get_by_username(post_request.user_name)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    post = Post()
    post.title = post_request.title
    post.content = post_request.content
    post.author_id = user.id
    post_repo.save(post)

    return PostResponse(
        message="ok",
        data=post
    )


@router.get("/posts/{user_name}",
            response_model=PostResponse)
async def get_user_posts(user_name: str, session_id: UUID = Depends(session_cookie)):
    session = session_manager.get(session_id)

    LOG.info("get_user_posts", user_name=user_name)
    LOG.info("session_data.username", session_data_username=session.username)
    session.foo = "bar"
    session_manager.update(session_id, session)

    user_repo = UserRepository()
    post_repo = PostRepository()

    user = user_repo.get_by_username(user_name)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    posts = post_repo.get_post_by_user(user)

    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Posts not found for this user")

    return PostResponse(
        message="ok",
        data=posts
    )



