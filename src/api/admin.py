  
import os
from flask_admin import Admin
from .models import db, User, Service1, Service2, Service3, BudgetItems
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Service1, db.session))
    admin.add_view(ModelView(Service2, db.session))
    admin.add_view(ModelView(Service3, db.session))
    # admin.add_view(ModelView(Service4, db.session))
    admin.add_view(ModelView(BudgetItems, db.session))
   