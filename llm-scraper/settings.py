import os

from dotenv import load_dotenv

load_dotenv()
open_ai_api_key = os.getenv('API_KEY')
