
import uvicorn
from fastapi import FastAPI
from fastapi_examples.handlers.blog_v1 import router as blog_v1
from fastapi_examples.handlers.sec_session_v1 import router as sec_session_v1
from intermediate_topics.sql.sqlalchemy.database import create_db

app = FastAPI()
app.include_router(blog_v1, prefix="/v1")
app.include_router(sec_session_v1, prefix="/v1")


@app.get("/ping")
def ping():
    return {"ping": "pong!"}


@app.on_event("startup")
def startup_event() -> None:
    create_db()


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
