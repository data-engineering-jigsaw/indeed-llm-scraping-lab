import os
from pathlib import Path

import numpy as np
import pandas as pd

from app import create_app, db
from app.models import *
from scraper.json_builder import *


def read_file(file):
    f = open(file, "r")
    text = f.read()
    return text

def file_to_df(file_name):
    pass

def parse_from_file_name(file_name):
    pass

def file_to_db(file_name, db_conn):
    app = create_app(db_conn)
    with app.app_context():
        pass

def files_to_db(file_names, db_conn):
    pass

def list_files(directory):
    file_names = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_names.append(os.path.join(root, file))
    return file_names

