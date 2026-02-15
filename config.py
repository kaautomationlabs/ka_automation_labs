import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_API_KEY = os.getenv('API_KEY')
TWITTER_API_SECRET = os.getenv('API_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
TWITTER_ACCESS_SECRET = os.getenv('ACCESS_SECRET')
OWM_KEY = os.getenv('OPENWEATHER_KEY')
