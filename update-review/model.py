import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(99), unique=True)

    dinosaurs = db.relationship("Dinosaur", backref="user", lazy=False)

    def __init__(self, username):
        self.username = username

class Dinosaur(db.Model):
    __tablename__ = "dinosaurs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(99), unique=True)
    herbivore = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __init__(self, name, herbivore, user_id):
        self.name = name
        self.herbivore = herbivore
        self.user_id = user_id


def connect_to_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    print("Connected...")

if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)


