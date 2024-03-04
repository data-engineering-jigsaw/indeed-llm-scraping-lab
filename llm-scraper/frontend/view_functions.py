import json

import pandas as pd
import requests

API_URL = "http://127.0.0.1:5000/positions"

def find_positions():
    response = requests.get(API_URL)
    json_dicts = json.loads(response.text)
    return pd.DataFrame(json_dicts)