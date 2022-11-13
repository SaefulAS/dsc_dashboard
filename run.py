import os
from flask_wtf.csrf import CSRFProtect
from app import create_app, db
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)
db = SQLAlchemy(app)
csrf = CSRFProtect(app)
if __name__ == '__main__':
    app.config['SECRET_KEY'] = "12345678"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://saefulas:eful2805@localhost/dashboard'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.run()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=True)

    def __init__(self, username, email, password, is_admin):
        self.username = username
        self.email = email
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        return '<User %r>' % self.username

admin = User('admin', 'admin@gmail.com', '1234', 1)

db.create_all() # In case user table doesn't exists already. Else remove it.    

db.session.add(admin)

db.session.commit() # This is needed to write the changes to database

User.query.all()

User.query.filter_by(username='admin').first()