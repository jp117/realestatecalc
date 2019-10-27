from flask_login import UserMixin
from realestatecalc import db, login
from flask import redirect, request

class User():
    def __init__(self, email):
        self.email = email

    def is_authenticated(self):
        return True

    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.email
    
    @login.user_loader
    def load_user(email):
        u = db.users.find_one({'email':email})
        if not u:
            return None
        return User(email=u['email'])

    
@login.unauthorized_handler
def unauthorized_callback():
    return redirect('/login?next=' + request.endpoint)


