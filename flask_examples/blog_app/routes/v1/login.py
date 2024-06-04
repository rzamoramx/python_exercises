
from flask import Blueprint, render_template, request, session, redirect, url_for
from repositories.user_repo import get_user

v1 = Blueprint('login v1', __name__, url_prefix='/v1')


def extend_app():
    @v1.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            user = get_user(username)
            if not user:
                return 'User not found'

            if user['password'] != password:
                return 'Invalid password'

            # Store the username in the session
            session['username'] = username
            return redirect(url_for('blog v1.profile'))

        return render_template('login.html')

    @v1.route('/logout', methods=['GET'])
    def logout():
        # Remove the 'username' key from the session
        session.pop('username', None)
        return redirect(url_for('login v1.login'))


    return v1
