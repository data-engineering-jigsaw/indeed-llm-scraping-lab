

from app import create_app, db
from app.models import Position, Scraping
from settings import dev_db

app = None

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Position': Position, 'Scraping': Scraping}

