from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import safe_str_cmp

db = SQLAlchemy()

#todo hash and salt passwords
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(200), unique=True,nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), nullable=True)
    budget_relationship = db.relationship('BudgetItems',backref='user',lazy=True)
    
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


class Service1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category=db.Column(db.String(100))
    #brand=db.Column(db.String(100))
    description=db.Column(db.String(100))
    provider=db.Column(db.String(100))
    phone=db.Column(db.String(100))
    price=db.Column(db.Integer)
    url = db.Column(db.String(400), nullable=True)
    budget_relationship=db.relationship('BudgetItems',backref='service1',lazy=True)
   
    def getAllService():
        list_serv = Service1.query.all()
        list_serv = list(map(lambda x: x.serialize(), list_serv))
        return(list_serv)

    def __repr__(self):
        return '<Srv1 %s>' % self.provider

    def serialize(self):
        return {
            "id": self.id,
            "category": self.category,
            #"brand": self.brand,
            "description": self.description,
            "provider": self.provider,
            "phone": self.phone,
            "price": self.price,
            "url": self.url,
        }

class Service2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category=db.Column(db.String(100))
    #brand=db.Column(db.String(100))
    description=db.Column(db.String(100))
    provider=db.Column(db.String(100))
    phone=db.Column(db.String(100))
    price=db.Column(db.Integer)
    url = db.Column(db.String(400), nullable=True)
    budget_relationship=db.relationship('BudgetItems',backref='service2',lazy=True)

    def getAllService():
        list_serv = Service2.query.all()
        list_serv = list(map(lambda x: x.serialize(), list_serv))
        return  (list_serv)
    
    def __repr__(self):
        return '<Srv2 %s>' % self.provider

    def serialize(self):
        return {
            "id": self.id,
            "category": self.category,
            #"brand": self.brand,
            "description": self.description,
            "provider": self.provider,
            "phone": self.phone,
            "price": self.price,
            "url": self.url,
        }

class Service3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category=db.Column(db.String(100))
    #brand=db.Column(db.String(100))
    description=db.Column(db.String(100))
    provider=db.Column(db.String(100))
    phone=db.Column(db.String(100))
    price=db.Column(db.Integer)
    url = db.Column(db.String(400), nullable=True)
    budget_relationship=db.relationship('BudgetItems',backref='service3',lazy=True)

    def getAllService():
        list_serv = Service3.query.all()
        list_serv = list(map(lambda x: x.serialize(), list_serv))
        return(list_serv)

    def __repr__(self):
        return '<Srv3 %s>' % self.provider

    def serialize(self):
        return {
            "id": self.id,
            "category": self.category,
            #"brand": self.brand,
            "description": self.description,
            "provider": self.provider,
            "phone": self.phone,
            "price": self.price,
            "url": self.url,
        }

class BudgetItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey(User.id))
    service1_id= db.Column(db.Integer,db.ForeignKey(Service1.id))
    service2_id= db.Column(db.Integer,db.ForeignKey(Service2.id))
    service3_id= db.Column(db.Integer,db.ForeignKey(Service3.id))
    #service4_id= db.Column(db.Integer,db.ForeignKey(Service4.id))
    
    def __repr__(self):
        return '<BudgetID %s>' % self.id

    def getAllBudget():
        list_budget = BudgetItems.query.all()
        list_budget = list(map(lambda x: x.serialize(), list_budget))
        return(list_budget)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "service1_id":self.service1_id,
            "service2_id":self.service2_id,
            "service3_id":self.service3_id,
            # do not serialize the password, its a security breach
        }


    
    
