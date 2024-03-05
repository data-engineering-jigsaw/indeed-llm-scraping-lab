import json
import os
from datetime import datetime

from scraper.file_reader import *
from scraper.indeed_scraper import (directory_name_builder,
                                    retrieve_and_write_pages)

position = 'data engineer'
location = 'United States'
idx = 0
retrieve_and_write_pages(position, location, pages = 5)
# generate_directory
# dir_to_db(dir_name)



