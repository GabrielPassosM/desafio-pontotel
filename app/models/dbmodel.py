from app import app
from flask_sqlalchemy import SQLAlchemy


app.config['DATABASE_URL'] = 'postgres://ccecbcuhcurema:94271a951c166a9408789f18cbdfc8280cc6aa4a2c48020a483d6c94b3da11a2@ec2-3-211-245-154.compute-1.amazonaws.com:5432/d6eejfo8l1uscq'
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
