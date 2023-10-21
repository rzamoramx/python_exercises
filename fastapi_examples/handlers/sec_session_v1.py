
import structlog
from uuid import uuid4, UUID
from fastapi import APIRouter, Response, Depends
from fastapi_examples.models.SessionData import SessionData
from fastapi_examples.security.session_manager import session_manager, session_cookie, session_verifier

router = APIRouter()
LOG = structlog.get_logger("sec_session_v1")


@router.get("/create_session/{user_name}")
async def create_session(user_name: str, response: Response):
    session_id = uuid4()
    session_data = SessionData(username=user_name)

    await session_manager.create(session_id, session_data)
    session_cookie.attach_to_response(response, session_id)

    return f"session created for user: {user_name}"


@router.get("/whoami", dependencies=[Depends(session_cookie)])
async def whoami(session_data: SessionData = Depends(session_verifier)):
    return session_data


@router.post("/delete_session")
async def del_session(response: Response, session_id: UUID = Depends(session_cookie)):
    await session_manager.delete(session_id)
    session_cookie.delete_from_response(response)
    return "deleted session"
