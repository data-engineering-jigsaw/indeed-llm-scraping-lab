import os
from pathlib import Path

import numpy as np
import pandas as pd
from app import create_app, db
from app.models import *
from scraper.json_builder import *


def file_to_df(file_name):
    file_text = read_file(file_name)
    if len(file_text) < 20:
        return pd.DataFrame()
    else:
        prompt = build_prompt(file_text)
        
        json_data = return_json_from(prompt)['jobs']
        df = pd.DataFrame(json_data)
        df = df.replace({np.nan: None, 'unknown': None, '': None})
        return df

def file_to_db(file_name):
    app = create_app()
    
    df = file_to_df(file_name)
    
    with app.app_context():
        scraping_attrs = parse_from_file_name(file_name)
        scraping = Scraping(**scraping_attrs)
        db.session.add(scraping)
        db.session.commit()
        
        for idx, row in df.iterrows():
            pos_attrs = row.to_dict()
            position = Position(**pos_attrs)
            position.scraping = scraping
            
            db.session.add(position)
            db.session.commit()

def parse_from_file_name(file_name):
    pref, relative_dir, docs, position, location, date, file_name_ext = file_name.split('/')
    file_name, ext = file_name_ext.split('.')
    prefix, idx = file_name.split('_')
    return {'position': position, 'location': location, 'date': date, 'job_idx': idx}

def list_files(directory):
    file_names = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_names.append(os.path.join(root, file))
    return file_names

# TODO change to dir_to_db
def dir_to_dfs(dir_name):
    file_names = list_files(dir_name)
    dfs = [file_to_df(file_name) for file_name in file_names]
    return list(zip(file_names, dfs))



def read_file(file):
    f = open(file, "r")
    text = f.read()
    return text







# first just save it to a directory
# first create the search, and save it
# then for each of the files, store the search id