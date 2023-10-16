
import unittest
import testing.postgresql
import intermediate_topics.sql.sqlalchemy.repositories.PostRepository as PostRepository
from intermediate_topics.sql.sqlalchemy.database import create_db


class PostRepositoryTest(unittest.TestCase):
    """
    This class is used to test the PostRepository class.
    Here we are using testing.postgresql to create a temporary PostgreSQL database. It's similar to H2 in Java.
    But is necessary to install PostgreSQL in your machine, otherwise you will get this error:
    "command not found: initdb"
    :(
    """
    pg_db = None

    def setUp(self):
        self.pg_db = testing.postgresql.Postgresql()
        create_db(self.pg_db.url())

    def tearDown(self):
        self.pg_db.stop()

    def test_save(self):
        post = PostRepository.Post(title='Post 1', content='Content of Post 1')
        repo = PostRepository.PostRepository()
        repo.save(post)

        self.assertEqual(post.title, 'Post 1')

