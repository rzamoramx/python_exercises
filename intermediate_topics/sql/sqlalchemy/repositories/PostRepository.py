
from intermediate_topics.sql.sqlalchemy.models.Post import Post
from intermediate_topics.sql.sqlalchemy.models.User import User
from intermediate_topics.sql.sqlalchemy.database import get_session


class PostRepository:
    _session = None

    def __init__(self):
        self._session = get_session()

    def save(self, data: Post):
        self._session.add(data)
        self._session.commit()

    def get_post_by_user(self, user: User) -> [Post]:
        return self._session.query(Post).filter_by(author=user).all()

    def get_all(self) -> [Post]:
        return self._session.query(Post).all()
