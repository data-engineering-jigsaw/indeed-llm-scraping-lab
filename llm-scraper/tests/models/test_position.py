import pytest
from app.models import Position, Scraping
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


def delete_records():
    db.session.query(Position).delete()
    db.session.query(Scraping).delete()

@pytest.fixture
def build_db():
    app = create_app()
    with app.app_context():
        delete_records(db)

        bartender = Bartender(name = 'moe', hometown = "springfield", birthyear = 1970)
        db.session.add(bartender)

def test_init_position():
    position = Position(*['8cba12eacacdf624', 'Data Engineer', [70, 73], 'Ana-Data Consulting Inc', 'New York', 'NY'])
    assert position.__dict__ == {'id': '8cba12eacacdf624', 'title': 'Data Engineer', 'min_salary': 70, 'max_salary': 73, 'city': 'Ana-Data Consulting Inc', 'state': 'New York', 'company_name': 'NY'}
    