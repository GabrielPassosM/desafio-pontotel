from app import app
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2gabriel1@localhost/alphaempresas'
db = SQLAlchemy(app)

class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    value = db.Column(db.String, nullable=False)

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return '<Empresa %r>' % self.name
