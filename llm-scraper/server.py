from flask import jsonify

from app import create_app, db
from app.models import Position, Scraping
from settings import dev_db

app = create_app(dev_db)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Position': Position, 'Scraping': Scraping}

@app.route('/positions')
def positions():
    positions = db.session.query(Position).all()
    positions_dicts = [position.to_dict() for position in positions]
    return jsonify(positions_dicts)