from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    u"postgresql://postgres:POSTGRES@localhost/hfgdb",)

metadata = MetaData()

user = Table('appuser', metadata,
    Column('appuser_id', Integer, primary_key=True),
    Column('username', String(200), nullable=False),
    Column('first_name', String(200), nullable=False),
    Column('last_name', String(200), nullable=False),
    Column('email_address', String(400), key='email'),
    Column('password', String(200), nullable=False)
)

r = metadata.create_all(engine)


print('ok',r)

'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

with app.app_context():
    db.create_all()
# http://stackoverflow.com/questions/28839587/how-do-i-create-a-table-in-postgresql-with-sqlalchemy
'''