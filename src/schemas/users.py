from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from src.database.models import User


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ['id', 'is_admin']
        load_instance = True
        load_only = ('password',)

    actors = Nested('UserSchema', many=True, exclude=('films',))
