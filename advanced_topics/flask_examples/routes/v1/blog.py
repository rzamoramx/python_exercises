
from flask import session, Blueprint, request

v1 = Blueprint('blog v1', __name__, url_prefix='/v1')


def extend_app():
    @v1.route('/profile', methods=['GET'])
    def profile():
        if 'username' in session:
            username = session['username']
            return f'Welcome, {username}! <a href="/v1/logout">Logout</a>'
        else:
            return 'Please log in first <a href="/v1/login">Login</a>'

    @v1.route('/update_profile', methods=['POST'])
    def update_profile():
        # Update username in session with value from form
        session['username'] = request.form['username']

        return f'Profile updated for {session["username"]}'

    @v1.route('/home' , methods=['GET'])
    def blog():
        return 'Blog page'

    @v1.route('/blog/<int:blog_id>' , methods=['GET'])
    def blog_post(blog_id):
        return f'Blog post {blog_id}'

    @v1.route('/blog/<int:blog_id>/comments' , methods=['GET'])
    def blog_comments(blog_id):
        return f'Comments for blog post {blog_id}'

    @v1.route('/blog/<int:blog_id>/comments/<int:comment_id>' , methods=['GET'])
    def blog_comment(blog_id, comment_id):
        return f'Comment {comment_id} for blog post {blog_id}'

    return v1
