import uuid
from src import db


class Film(db.Model):
    __tablename__ = 'films'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    release_date = db.Column(db.Date, nullable=False, index=True)
    uuid = db.Column(db.String(36), unique=True)
    description = db.Column(db.Text)
    distributed_by = db.Column(db.String(120), nullable=False)
    length = db.Column(db.Float)
    rating = db.Column(db.Float)

    def __init__(self, title, release_date, description, distributed_by, length, rating):
        self.title = title
        self.release_date = release_date
        self.description = description
        self.distributed_by = distributed_by
        self.length = length
        self.rating = rating
        self.uuid = str(uuid.uuid4())

    def __repr__(self):  # метод для отладки
        return f'Film({self.title}, {self.uuid}, {self.distributed_by}, {self.release_date})'

    def to_dict(self):  # метод для используемый в качестве сериализатора
        return {
            'title': self.title,
            'uuid': self.uuid,
            'release_date': self.release_date.strftime('%Y-%m-%d'),
            'description': self.description,
            'distributed_by': self.distributed_by,
            'length': self.length,
            'rating': self.rating
        }


class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    uuid = db.Column(db.String(36), unique=True)
    description = db.Column(db.Text)

    def __init__(self, first_name, last_name, description):
        self.first_name = first_name
        self.last_name = last_name
        self.description = description

    def __repr__(self):
        return f'Actor({self.first_name}, {self.last_name}, {self.uuid})'

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            'uuid': self.uuid,
            'description': self.description

        }
