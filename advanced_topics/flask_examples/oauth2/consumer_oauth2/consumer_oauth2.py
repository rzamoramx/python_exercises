
import requests
import jwt
from datetime import datetime
from flask import Flask, jsonify, url_for, redirect, request, render_template, session
"""
Simple demo for app consumer of Oauth2 (flow)
"""

app = Flask(__name__)
app.secret_key = '12345678'
client_id = 'my-client-id'
client_secret = '12345678'
# this is to prevent CSRF attacks in a real scenario we should generate a random string and save it in the session
# cookie or in the database
state = '1234'


def refresh_token() -> str:
    # refresh the access token
    refresh_token_url = 'http://localhost:8081/token' + \
                        '?client_id=' + client_id + \
                        '&refresh_token=' + session.get('refresh_token') + \
                        '&grant_type=refresh_token'
    refresh_token_response = requests.post(refresh_token_url)
    return refresh_token_response.json()['access_token']


@app.route('/request_auth', methods=['GET', 'POST'])
def request_auth():
    print(f'request method: {request.method}')
    if request.method == 'POST':
        # Note: we should to generate a random string as state to prevent CSRF attacks
        # 2 - Create an authorization url and redirect the user to it
        auth_url = 'http://localhost:8081/authorize' + \
                   '?client_id=' + client_id + \
                   '&redirect_uri=http://localhost:8080/callback' + \
                   '&response_type=code' + \
                   '&scope=email' + \
                   '&state=' + state
        return redirect(auth_url)

    # 1 - Request to user to authorize the app
    return render_template('request_auth_url.html')


@app.route('/callback')
def callback():
    # 6 - Handle the authorization code
    authorization_code = request.args.get('code')

    # This is to prevent CSRF attacks
    print(f'state: {request.args.get("state")}')
    print(f'var state: {state}')
    if request.args.get('state') != state:
        return jsonify({'error': 'Invalid state parameter'}), 401

    # Exchange authorization code for access token
    access_token_url = 'http://localhost:8081/token' + \
                        '?client_id=' + client_id + \
                        '&code=' + authorization_code + \
                        '&grant_type=authorization_code'

    # 7 - Make a POST request to the access token endpoint
    access_token_response = requests.post(access_token_url)

    # 9 - Get the access token from the response
    # We can save the access token in a session cookie for future usage
    # NOTE: this is not a secure way to store access tokens, it is only for demonstration purposes
    # NOTE 2: the refresh token basically is an access token with a longer expiration time, it is important to
    # save the refresh token in a secure way to prevent attackers from stealing it and using it to request new
    # access tokens because we give them a big time window to do so
    session['access_token'] = access_token_response.json()['access_token']
    session['refresh_token'] = access_token_response.json()['refresh_token']

    return redirect(url_for('me'))


@app.route('/app/me')
def me():
    # Get the access token from the session cookie
    print(f'access_token: {session.get("access_token")}')

    # decode the access token
    decoded_access_token = jwt.decode(session.get('access_token').encode('utf-8'),
                                      client_secret, algorithms=["HS256"])

    # check if the access token has expired
    if datetime.utcfromtimestamp(decoded_access_token['exp']) < datetime.utcnow():
        session['access_token'] = refresh_token()

    # 10 - Use the access token to fetch the user's profile data or any other data from the API server
    user_profile_url = 'http://localhost:8081/api/me'

    # Make a GET request to the API server
    # send access token as header: Authorization
    user_profile_response = requests.get(user_profile_url, headers={'Authorization': 'Bearer ' + session.get('access_token')})

    print(f'user_profile_response: {user_profile_response.text}')

    # Return the profile data as JSON
    return jsonify(user_profile_response.json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
