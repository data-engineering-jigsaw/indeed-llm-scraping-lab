import json
import os
from datetime import datetime


from scraper.file_reader import *
from scraper.indeed_scraper import (directory_name_builder,
                                    retrieve_and_write_pages)

position = 'data engineer'
location = 'United States'
idx = 0


# dir_name = directory_name_builder(position, location, date = 'today')
# files_dfs = dir_to_dfs(dir_name)
directory = './data/text_docs'
files = list_files(directory)
file_name = files[0]
file_to_db(file_name)



# # experience level (if unknown say unknown)
# json_data = json.loads(response.response)
# get the id
# notice that experience level does not work too well
# and probably should parse from there
# from here, we can write to json
# integrate sqlalchemy and flask




