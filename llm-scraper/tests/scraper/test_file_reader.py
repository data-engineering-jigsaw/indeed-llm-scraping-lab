import pdb
from datetime import date

import pytest
from bs4 import BeautifulSoup as bs

from scraper.file_reader import *


def test_file_to_df():
    file_name = "./data/sample/example/results_0.txt"
    df = file_to_df(file_name)
    records = [{'job_id': 'e786e718fef6eccf', 'job_title': 'Data Center Engineer', 'company_name': 'PAYLOCITY CORPORATION', 'seniority_level': None, 'min_salary': 62000.0, 'max_salary': 117000.0,
     'city': 'Schaumburg', 'state': 'IL', 'zipcode': '60173', 'presence': None},
     {'job_id': 'bd1c7f18f0faf355', 'job_title': 'Data Engineer', 'company_name': 'Archer Daniels Midland Company', 'seniority_level': None, 'min_salary': None, 'max_salary': None, 'city': 'Erlanger', 
     'state': 'KY', 'zipcode': None, 'presence': None}]
    assert df.to_dict('records') == records

def test_dir_to_dfs():
    dir_name = "./data/sample/example/"
    filenames_dfs = dir_to_dfs(dir_name)
    len(filenames_dfs) == 2
    first_filename_df = filenames_dfs[0]
    assert first_filename == 'results_0.txt'

def test_parse_from_file_name():
    file_name = "./data/text_docs/data_engineer/united_states/2024-03-01/results_2.txt"
    parsed_dict = parse_from_file_name(file_name)
    assert parsed_dict == {'position': 'data_engineer', 'location': 'united_states',
     'date': '2024-03-01', 'job_idx': '2'}


