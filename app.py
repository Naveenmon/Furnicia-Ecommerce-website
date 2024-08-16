from flask import *

from user.user import user

app = Flask(__name__)
app.register_blueprint(user, url_prefix='/')
app.config.from_object(Config)
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = "filesystem"

if __name__ == '__main__':
    app.secret_key = 'navi123'
    app.run(debug=True, port=5005)
