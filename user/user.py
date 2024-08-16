from flask import *

user = Blueprint('user', __name__, template_folder='templates', static_folder='static', static_url_path='/user')

from user.route import *


