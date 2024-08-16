from bson import ObjectId

from user.models import *
from user.user import user
from flask import *


@user.route('/')
def index():
    if not session.get("name"):
        return render_template('index.html')
    else:
        return render_template('index.html')


@user.route('/logout')
def logout():
    session['name'] = None
    session["id"] = None
    session.clear()
    return redirect(url_for('user.index'))


@user.route('/shop')
def shop():
    res = mongo[db]['products'].find({})
    result = fetch(res)
    return render_template('shop.html', l=result)


@user.route('/product')
def product():
    return render_template('shop-detail.html')


@user.route('/shop-detail/<string:id>')
def shop_detail(id):
    oid = ObjectId(id)
    res = mongo[db]['products'].find({'_id': oid})
    result = fetch(res)
    return render_template('shop-detail.html', r=result)


@user.route('/check')
def check():
    return render_template('checkout.html')


@user.route('/signup')
def signup():
    return render_template('signup.html')


@user.route('/signin')
def signin():
    return render_template('signin.html')


@user.route('/signin/user', methods=['GET', 'POST'])
def signin_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        res = mongo[db]['users'].find({'email': email, 'password': password})
        result = fetch(res)
        if len(result) == 1:
            session["id"] = str(result[0]['_id'])
            session["name"] = result[0]['username'].upper()
            return redirect(url_for('user.index'))
        else:
            return redirect(url_for('user.signin'))

    else:
        return render_template('signin.html')


@user.route('/signup/user', methods=['GET', 'POST'])
def signup_user():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['cpassword']
        if password == cpassword:
            s = userdetails(username, email, password, cpassword)
            mongo[db]['users'].insert_one(s.user)
            del s
            return redirect(url_for('user.signin'))
        else:
            return render_template('signup.html')
    return render_template('signup.html')


@user.route('/addcart/<string:id>', methods=['GET', 'POST'])
def addcart():
    return render_template('cart.html')