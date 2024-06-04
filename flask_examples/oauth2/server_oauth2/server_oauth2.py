
from datetime import datetime, timedelta
from flask import Flask, request, jsonify, redirect, render_template, url_for, session
from functools import wraps
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import jwt

"""
Simple demo for server Oauth2 (flow) 
"""
JWT_EXPIRY_TIME = 600
JWT_REFRESH_EXPIRY_TIME = 3600
login_manager = LoginManager()
auth_codes = {}
access_tokens = {}
refresh_tokens = {}
clients = {
    'my-client-id': {'client_secret': '12345678'}  # the client_secret is generated per app that will be authorized
}
users = {
    '123124': {'username': 'testuser', 'password': 'password', 'client_id': 'my-client-id'},
}


class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @property
    def is_active(self):
        return True

    def get_id(self):
        return self.id

    def check_password(self, password):
        return True if password == self.password else False


@login_manager.user_loader
def load_user(user_id: str) -> User:
    # Load the user from the database
    if user_id in users:
        user = User(user_id, users[user_id]['username'], users[user_id]['password'])
        return user
    return None


def user_by_username(username: str) -> User:
    for user_id, user in users.items():
        if user['username'] == username:
            return User(user_id, user['username'], user['password'])
    return None


def user_by_client_id(client_id: str) -> User:
    for user_id, user in users.items():
        if user['client_id'] == client_id:
            return User(user_id, user['username'], user['password'])
    return None


def generate_tokens(client_id: str) -> (str, str):
    """ NOTE: the refresh token scenarios is a little bit more complex, these are the scenarios typically used:
        Refresh Token Rotation: In a more secure setup, some authorization servers implement a technique called
        "refresh token rotation." In this approach, when a client uses a refresh token to obtain a new access token,
        the server may issue a new refresh token alongside the new access token. This practice helps mitigate the risk
        associated with long-lived refresh tokens.

        No Refresh Token Renewal: Some authorization servers do not issue new refresh tokens when you use a refresh
        token to obtain a new access token. In this case, the original refresh token continues to be used until it
        expires or is revoked.

        Limited Refresh Token Lifetime: In some configurations, refresh tokens have a limited lifetime. They may be
        valid for a certain number of uses or for a specific duration. When they expire or reach their usage limit, the
        client must re-authenticate to obtain a new refresh token.

        In this example we are using the first because we generate a new refresh token every time that the user
        request a new access token
    """
    # Generate a JWT token
    access_token = jwt.encode(
        {
            "exp": datetime.utcnow() + timedelta(seconds=JWT_EXPIRY_TIME),
            "sub": client_id,
            "scope": "user_profile",
        },
        clients[client_id]['client_secret'],
        algorithm="HS256",
    )

    # Generate a refresh token
    refresh_token = jwt.encode(
        {
            "exp": datetime.utcnow() + timedelta(seconds=JWT_REFRESH_EXPIRY_TIME),
            "sub": client_id,
            "scope": "user_profile",
        },
        clients[client_id]['client_secret'],
        algorithm="HS256",
    )

    return access_token, refresh_token


def load_user_from_token(fn):
    @wraps(fn)
    def decorated(*args, **kwargs):
        # This is not the right way to handle user data, it is only for demonstration purposes
        if 'Authorization' not in request.headers:
            return jsonify({'error': 'Missing authorization header'}), 401

        access_token = request.headers['Authorization'].split(' ')[1]
        print(f'tokens: {auth_codes}')

        if access_token in access_tokens:
            user = user_by_client_id(access_tokens[access_token]['client_id'])
            if not user:
                return jsonify({'error': 'User not found'}), 401
            return fn(user)

        for _, client in access_tokens.items():
            print(f'client: {client}')
            if client == access_token:
                user = user_by_client_id(client['client_id'])
                if not user:
                    return jsonify({'error': 'User not found'}), 401
                return fn(user)
        return fn(None)
    return decorated


# Define the oauth2_required() decorator
def oauth2_required(fn):
    @wraps(fn)
    def decorated(*args, **kwargs):
        # Get the access token from the request
        print(f'request.headers: {request.headers}')

        if 'Authorization' not in request.headers:
            return jsonify({'error': 'Missing authorization header'}), 401

        # Validate the access token
        # maybe we should validate expiration too, but it is a simple example
        if not request.headers['Authorization'].split(' ')[1] in access_tokens:
            return jsonify({'error': 'Invalid access token'}), 401

        # The access token is valid, so call the original function
        return fn(*args, **kwargs)
    return decorated


app = Flask(__name__)
app.secret_key = '12345678'
login_manager.init_app(app)


# +++++++++++++++++++++++++++++++++ Protected resources ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@app.route('/api/me', methods=['GET'])
@oauth2_required
@load_user_from_token
def get_api_data(user):
    print(f'user: {user}')

    if user:
        return jsonify({'data': {'user_name': user.username, 'other_sensitive_data': 'Foo Bar'}})
    return jsonify({'error': 'Invalid access token'}), 401


# this can be only accessed if the user is logged in and is using the portal of this server
@app.route('/dashboard')
@login_required
def dashboard():
    username = current_user.username
    return render_template("dashboard.html", username=username)


# ++++++++++++++++++++++++++++++++ Endpoints to handle session ++++++++++++++++++++++++++++++++++++++++++++++++
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Validate the user credentials
        user = user_by_username(username)
        if not user:
            return render_template("login_for_oauth.html", message="Username not found")
        elif user.password != password:
            return render_template("login_for_oauth.html", message="Invalid password")
        else:
            login_user(user)
            if session.get('authorizing'):
                return redirect(url_for("authorize", client_id=session.get('client_id'),
                                        scope=session.get('scope'), redirect_uri=session.get('redirect_uri'),
                                        response_type=session.get('response_type'), state=session.get('state')))
            redirect(url_for("dashboard"))
    else:
        return render_template("login_for_oauth.html", message="Please login")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


# +++++++++++++++++++++++++++++++++++++++ Endpoints to handle OAuth2 flow ++++++++++++++++++++++++++++++++++++++
@app.route('/authorize', methods=['GET', 'POST'])
def authorize():
    if not request.args.get('client_id') or not request.args.get('scope') or \
            not request.args.get('redirect_uri') or not request.args.get('response_type') or \
            not request.args.get('state'):
        return jsonify({'error': 'Missing params'}), 401

    # 3 - if user isn't logged in, redirect to login page
    if not current_user.is_authenticated:
        # save temporarily params in session
        session['client_id'] = request.args.get('client_id')
        session['scope'] = request.args.get('scope')
        session['redirect_uri'] = request.args.get('redirect_uri')
        session['response_type'] = request.args.get('response_type')
        session['state'] = request.args.get('state')
        session['authorizing'] = True

        return redirect(url_for('login'))

    if request.method == 'POST':
        # 5 - Generate authorization code and redirect to the client callback
        if request.args.get('client_id') not in clients:
            return jsonify({'error': 'Invalid client_id or invalid client_secret'}), 401

        # some other validations for example if the user has access to the requested scope, etc.

        # save code in our "database", this is not the right way to store authorization codes
        # it is only for demonstration purposes
        authorization_code = jwt.encode(
            {
                "exp": datetime.utcnow() + timedelta(seconds=600),
                "sub": request.args.get('client_id'),
            },
            clients[request.args.get('client_id')]['client_secret'],
            algorithm="HS256",
        )
        auth_codes[authorization_code] = {'client_id': request.args.get('client_id')}

        # Delete all the temporary params from the session
        #session.clear()

        # Redirect to the client
        return redirect(request.args.get('redirect_uri') + '?code=' + authorization_code + '&state=' +
                        request.args.get('state'))

    # 4 - if user is logged in, show them the approval page
    return render_template('authorize.html', **request.args)


@app.route('/token', methods=['POST'])
def token():
    # 8 - Exchange authorization code for access token
    if not request.args.get('client_id'):
        return jsonify({'error': 'Missing client_id'}), 401

    if request.args.get('client_id') not in clients:
        return jsonify({'error': 'Invalid client_id'}), 401

    if not request.args.get('code') in auth_codes:
        return jsonify({'error': 'Invalid authorization code or refresh token'}), 401

    if request.args.get('grant_type') == 'authorization_code':
        authorization_code = request.args.get("code")

        # Decode the authorization code
        decoded_authorization_code = jwt.decode(authorization_code.encode('utf-8'),
                                                clients[request.args.get('client_id')]['client_secret'],
                                                algorithms=["HS256"])

        # Check if the authorization code is expired
        if datetime.utcfromtimestamp(decoded_authorization_code["exp"]) < datetime.utcnow():
            # here we should delete the authorization code from our "database" (access_tokens) and update the
            # auth_codes dictionary to reflect that the authorization code is expired, but it is only for
            # demonstration purposes
            raise Exception("Expired authorization code")

        # Check if the authorization code has a valid client_id
        if not decoded_authorization_code["sub"] in clients:
            raise Exception("Invalid client_id")

        # NOTE: the refresh token is optionally, and it is not mandatory in Oauth2, it depends
        # on our needs, for example if we not implement a refresh token it means that the
        # client will need to ask the user to authorize the app again
        access_token, refresh_token = generate_tokens(request.args.get('client_id'))

        # Save the access tokens
        access_tokens[access_token] = {'access_token': access_token, 'client_id': request.args.get('client_id')}
        refresh_tokens[refresh_token] = refresh_token

        # Return the access token
        return jsonify({'access_token': access_token, 'refresh_token': refresh_token, 'token_type': 'bearer'})

    elif request.args.get('grant_type') == 'refresh_token':
        refresh_token = request.args.get("refresh_token")

        if not refresh_token in refresh_tokens:
            return jsonify({'error': 'Invalid refresh token'}), 401

        # Decode the refresh token
        decoded_refresh_token = jwt.decode(refresh_token.encode('utf-8'),
                                           clients[request.args.get('client_id')]['client_secret'],
                                           algorithms=["HS256"])

        # Check if the refresh token is expired
        if datetime.utcfromtimestamp(decoded_refresh_token["exp"]) < datetime.utcnow():
            # here we should delete the refresh token from our "database" (access_tokens) and update the
            # refresh_tokens dictionary to reflect that the refresh token is expired, but it is only for
            # demonstration purposes
            raise Exception("Expired refresh token")

        # Check if the refresh token has a valid client_id
        if not decoded_refresh_token["sub"] in clients:
            raise Exception("Invalid client_id")

        # Generate a new access token
        access_token, refresh_token = generate_tokens(request.args.get('client_id'))

        # Save the access tokens
        access_tokens[access_token] = access_token
        refresh_tokens[refresh_token] = refresh_token

        # Return the access token
        return jsonify({'access_token': access_token, 'refresh_token': refresh_token, 'token_type': 'bearer'})

    else:
        return jsonify({'error': 'Invalid grant_type'}), 401


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8081)
