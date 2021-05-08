import pathlib


BASE_DIR = pathlib.Path(__file__).parent  # указываем родителя


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR/"data"/'imdb.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATION = False  # функция сигнализирующая когда происходят изменения в БД (отключена)
