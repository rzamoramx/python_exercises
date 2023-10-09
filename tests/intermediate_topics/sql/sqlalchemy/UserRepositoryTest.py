
import unittest
from unittest.mock import patch
from intermediate_topics.sql.sqlalchemy.repositories.UserRepository import UserRepository
from intermediate_topics.sql.sqlalchemy.models.User import User
from intermediate_topics.sql.sqlalchemy.database import create_db


class UserRepositoryTest(unittest.TestCase):
    def setUp(self):
        create_db()

    @patch('intermediate_topics.sql.sqlalchemy.repositories.PostRepository.PostRepository')
    def test_save(self, _):
        user = User(username='user1', email='user1@email.com', password='password1')
        repo = UserRepository()
        repo.save(user)

        self.assertEqual(user.username, 'user1')

    @patch('intermediate_topics.sql.sqlalchemy.repositories.PostRepository.PostRepository')
    def test_get_by_username(self, _):
        repo = UserRepository()

        # first create user and save it to continue with the test
        user = User(username='user2', email='user2@email.com', password='password2')
        repo.save(user)

        result = repo.get_by_username('user2')
        
        self.assertEqual(result.username, 'user2')
        self.assertEqual(result.email, 'user2@email.com')

    @patch('intermediate_topics.sql.sqlalchemy.repositories.PostRepository.PostRepository')
    def test_get_all(self, _):
        repo = UserRepository()

        # first create users and save them to continue with the test
        users = [
            User(username='user3', email='user3@email.com', password='password3'),
            User(username='user4', email='user4@email.com', password='password4')
        ]
        for user in users:
            repo.save(user)
        
        result = repo.get_all()
        
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].username, 'user3')
        self.assertEqual(result[1].username, 'user4')
