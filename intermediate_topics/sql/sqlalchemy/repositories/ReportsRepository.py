
from intermediate_topics.sql.sqlalchemy.database import get_session
from intermediate_topics.sql.sqlalchemy.models.Post import Post
from sqlalchemy.orm import joinedload


class ReportsRepository:
    _session = None

    def __init__(self):
        self._session = get_session()

    def get_posts_and_owner(self) -> list:
        return self._session.query(Post).options(joinedload(Post.author)).all()

