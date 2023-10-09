
from intermediate_topics.sql.sqlalchemy.models.User import User
from intermediate_topics.sql.sqlalchemy.database import get_session


class UserRepository:
    _session = None

    def __init__(self):
        self._session = get_session()

    def save(self, data: User):
        self._session.add(data)
        self._session.commit()

    def get_by_username(self, user: str) -> User:
        return self._session.query(User).filter(User.username == user).first()

    def get_all(self) -> [User]:
        return self._session.query(User).all()
