
from intermediate_topics.sql.sqlalchemy.models.User import User
from intermediate_topics.sql.sqlalchemy.models.Post import Post
from intermediate_topics.sql.sqlalchemy.database import create_db
from intermediate_topics.sql.sqlalchemy.repositories.PostRepository import PostRepository
from intermediate_topics.sql.sqlalchemy.repositories.UserRepository import UserRepository
from intermediate_topics.sql.sqlalchemy.repositories.ReportsRepository import ReportsRepository

user_repository = UserRepository()
post_repository = PostRepository()


def query_users_posts_reports():
    # Get all users
    print("********** Users **********")
    users = user_repository.get_all()
    for user in users:
        print(f'Username: {user.username}, Email: {user.email}, Password: {user.password}')

    # Get a user
    print("********** User by user name **********")
    user = user_repository.get_by_username('user1')
    print(f'Username: {user.username}, Email: {user.email}, Password: {user.password}')

    # Get all posts
    print("********** Posts **********")
    posts = post_repository.get_all()
    for post in posts:
        print(f'Title: {post.title}, Author: {post.author.username}, Content: {post.content}')

    # Get all posts by user
    print("********** Posts by User **********")
    posts = post_repository.get_post_by_user(users[0])
    for post in posts:
        print(f'Title: {post.title}, Author: {post.author.username}, Content: {post.content}')

    # Get all posts and their authors
    print("********** Posts and their authors **********")
    posts = ReportsRepository().get_posts_and_owner()
    for post in posts:
        print(f"Title: {post.title}, Email: {post.author.email}")


def create_users_posts():
    # Create users
    user1 = User(username='user1', email='user1@email.com', password='password1')
    user_repository.save(user1)
    user2 = User(username='user2', email='user2@email.com', password='password2')
    user_repository.save(user2)

    # Create posts
    post1 = Post(title='Post 1', content='Content of Post 1', author=user1)
    post_repository.save(post1)
    post2 = Post(title='Post 2', content='Content of Post 2', author=user2)
    post_repository.save(post2)


if __name__ == '__main__':
    create_db()
    create_users_posts()
    query_users_posts_reports()
