from simple_app import db


class UserProfile(db.Model):
    __tablename__ = 'profile'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    lastname = db.Column(db.String())
    firstname = db.Column(db.String())
    perms = db.Column(db.Integer, default=0)

    def __init__(self, username, password, lastname, firstname):
        self.username = username
        self.password = password
        self.lastname = lastname
        self.firstname = firstname
