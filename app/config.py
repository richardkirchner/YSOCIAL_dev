from dotenv import load_dotenv
from os import environ
load_dotenv()

SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')

EVENTS_MAX_PER_PAGE = 5

SECRET_KEY = environ.get('SECRET_KEY')
