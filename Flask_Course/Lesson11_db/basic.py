import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#this __file__ will automatically be set to the name of the file. Then this code finds the directory name of the actual file. This is particularly important b/c it ensures this works on windows, mac, linux, etc.
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

### SET UP THE DATABSE

#this sets up our database here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')


#we set this so we don't track modifications to our database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

# SET UP OUR MODEL (i.e. our table in the DB)
class Puppy(db.Model):

    # Manual table name choice
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        return f"Puppy {self.name} is {self.age} year/s old"