import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    MONGO_URI = os.getenv('MONGO_URI')
    APPLE_MUSIC_API_KEY = os.getenv('APPLE_MUSIC_API_KEY')