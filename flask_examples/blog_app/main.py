
from flask import Flask
from routes.v1.login import extend_app as login_v1
from routes.v1.blog import extend_app as blog_v1


app = Flask(__name__)
app.secret_key = "super secret key"


@app.route('/ping')
def ping():
    return {"ping": "pong!"}


app.register_blueprint(login_v1())
app.register_blueprint(blog_v1())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
