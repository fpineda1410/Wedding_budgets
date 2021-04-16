from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import safe_str_cmp

db = SQLAlchemy()

#todo hash and salt passwords
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=True)
    favorite_color = db.relationship('FavoriteColor',backref='user',lazy=True)
    
    def __repr__(self):
        return '<User %s>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    # todo Hash and Salt Passwords
    def check_password(self, password):
        return safe_str_cmp(password, self.password)

class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color=db.Column(db.String(100))
    favorite_color = db.relationship('FavoriteColor',backref='color',lazy=True)
    
    def __repr__(self):
        return '<Color %s>' % self.color

    def serialize(self):
        return {
            "id": self.id,
            "color": self.color,
            # do not serialize the password, its a security breach
        }



class FavoriteColor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey(User.id))
    color_id=db.Column(db.Integer,db.ForeignKey(Color.id))
    
    def __repr__(self):
        return '<Color %s>' % self.color_id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "color_id": self.color_id
            # do not serialize the password, its a security breach
        }