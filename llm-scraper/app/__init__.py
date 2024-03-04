from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    conn_str = "postgresql://localhost:5432/indeed_llm_scraper"
    app.config['SQLALCHEMY_DATABASE_URI'] = conn_str
    db.init_app(app)
    return app