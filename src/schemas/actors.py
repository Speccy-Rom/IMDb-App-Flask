from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from src.database.models import Actor


class ActorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Actor
        exclude = ['id']
        load_instance = True
