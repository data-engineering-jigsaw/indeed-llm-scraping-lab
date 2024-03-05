from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(db_conn):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_conn
    db.init_app(app)
    return app