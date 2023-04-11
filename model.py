import os
from flask_sqlalchemy import SQLAlchemy #imports SQLAlchemy


db = SQLAlchemy() #instantiates SQLAlchemy and saves it to the variable "db".

class User(db.Model): #creates the "User" class, wwhich is inherited from "Model".
    
    __tablename__ = "users" #names the table
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #creates the id column in my Users table
    username = db.Column(db.String(255), unique=True, nullable=False) #creates the username column, with a required unique username
    password = db.Column(db.String(255), nullable=False) #creates the password column, with a required password

class Team(db.model): #creates the "Team" class, whic is inherited from "Model".
    
    __tablename__ = "teams" #names the table.
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #creates column
    team_name = db.Column(db.String(255), unique=True, nullable=False) #creates column
    user_id = db.Column(db.Integer, db.foreign_key("users.id"), nullable=False) #references users table for information on users_id
    
class Project(db.Model): #creates Project class, inherited from "Model".
    
    __tablename__ = "projects" #names the table
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    completed = db.Column(db.Boolean, default=False)
    team_id = db.Column(db.Integer, db.Foreign_key("teams.id"), nullable=False)
    
def connect_to_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["POSTGRES-URI"] #first 2 lines set config attributes within Flask app.
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app #lines last 2 lines connect Flask instance to Flask-SQLAlchemy instance. This is the same as passing Flask app in at the top.
    db.init_app(app)
   
if __name__ == "__main__": #first 2 lines create Flask instance, same as importin Flask at the top.
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)
    print("Connected to db...")
