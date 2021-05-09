from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from src.database.models import Film


class FilmSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Film
        exclude = ['id']
        load_instance = True