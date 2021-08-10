import os
import pathlib


BASE_DIR = pathlib.Path(__file__).parent  # указываем родителя


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + str(
        BASE_DIR / "data" / "speccy.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'you-will-never-know'
    # SQLALCHEMY_ECHO = True
    HEROKU_DATABASE_URI = ''