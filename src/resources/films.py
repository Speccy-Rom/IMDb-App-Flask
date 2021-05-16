from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.orm import joinedload, selectinload


from src import db
from src.database.models import Film
from src.schemas.films import FilmSchema
from src.services.film_services import FilmServices


class FilmListApi(Resource):
    film_schema = FilmSchema()

    def get(self, uuid=None):
        if not uuid:
            films = FilmServices.fetch_all_films(db.session).options(
                selectinload(Film.actors))
            return self.film_schema.dump(films, many=True), 200
        film = FilmServices.fetch_all_by_uuid(db.session, uuid)
        if not film:
            return "", 404
        return self.film_schema.dump(film), 200

    def post(self):
        try:
            film = self.film_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(film)
        db.session.commit()
        return self.film_schema.dump(film), 201

    def put(self, uuid):
        film = FilmServices.fetch_all_by_uuid(db.session, uuid)
        if not film:
            return "", 404
        try:
            film = self.film_schema.load(request.json, instance=film, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(film)
        db.session.commit()
        return self.film_schema.dump(film), 200

    def patch(self, uuid):
        pass

    def delete(self, uuid):
        film = FilmServices.fetch_all_by_uuid(db.session, uuid)
        if not film:
            return "", 404
        db.session.delete(film)
        db.session.commit()
        return '', 204
