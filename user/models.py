from pymongo import MongoClient

mongo = MongoClient('localhost', 27017)
role = "user"
db = "Furni"


class userdetails:
    user = {}

    def __init__(self, name, email, password, cpassword):
        self.user['username'] = name
        self.user['email'] = email
        self.user['password'] = password
        self.user['cpassword'] = cpassword
        self.user['role'] = role
        self.user['wishlist'] = []
        self.user['cart'] = []


class productdetails:
    products = {}

    def __init__(self, name, description, price, image):
        self.products['name'] = name
        self.products['description'] = description
        self.products['price'] = price
        self.products['image'] = image


def fetch(r):
    l = []
    for i in r:
        l.append(i)
    return l