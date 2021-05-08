import datetime

from flask import request
from flask_restful import Resource

from src import api, db
from src.models import Film, Actor


class Smoke(Resource):
    def get(self):
        return {'message': 'OK'}


class FilmListApi(Resource):

    def get(self, uuid=None):
        if not uuid:
            films = db.session.query(Film).all()
            return [f.to_dict() for f in films], 200
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return "", 404
        return film.to_dict(), 200

    def post(self):
        film_json = request.json
        if not film_json:
            return {'message': 'Wrong data'}, 400
        try:
            film = Film(
                title=film_json['title'],
                release_date=datetime.datetime.strptime(film_json['release_date'], '%B %d, %Y'),
                distributed_by=film_json['distributed_by'],
                rating=film_json.get('rating'),
                length=film_json.get('length'),
                description=film_json.get('description')
            )
            db.session.add(film)
            db.session.commit()
        except (ValueError, KeyError):
            return {'message': 'Wrong data'}, 400
        return {'message': 'Created successfully', 'uuid': film.uuid}, 201

    def put(self, uuid):
        film_json = request.json
        if not film_json:
            return {'message': 'Wrong data'}, 400
        try:
            db.session.query(Film).filter_by(uuid=uuid).update(
                dict(
                    title=film_json['title'],
                    release_date=datetime.datetime.strptime(film_json['release_date'], '%B %d, %Y'),
                    distributed_by=film_json['distributed_by'],
                    rating=film_json.get('rating'),
                    length=film_json.get('length'),
                    description=film_json.get('description')
                )
            )
            db.session.commit()
        except (ValueError, KeyError):
            return {'message': 'Wrong data'}, 400
        return {'message': 'Updated successfully'}, 200

    def patch(self, uuid):
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return "", 404
        film_json = request.json
        title = film_json.get('title')
        release_date = datetime.datetime.strptime(film_json.get('release_date'), '%B %d, %Y') if film_json.get(
            'release_date') else None
        distributed_by = film_json.get('distributed_by')
        rating = film_json.get('rating')
        length = film_json.get('length')
        description = film_json.get('description')

        if title:
            film.title = title
        elif release_date:
            film.release_date = release_date
        elif distributed_by:
            film.distributed_by = distributed_by
        elif rating:
            film.rating = rating
        elif length:
            film.length = length
        elif description:
            film.description = description

        db.session.add(film)
        db.session.commit()
        return {'message': 'Updated successfully'}, 200

    def delete(self, uuid):
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return "", 404
        db.session.delete(film)
        db.session.commit()
        return '', 204



class ActorListApi(Resource):
    def get(self, uuid=None):
        if not uuid:
            actors = db.session.query(ActorListApi).all()
            return [f.to_dict() for f in actors], 200
        actor = db.session.query(ActorListApi).filter_by(uuid=uuid).first()
        if not actor:
            return '', 404
        return actor.to_dict(), 200

    def post(self):
        actor_json = request.json
        if not actor_json:
            return {'message': 'Wrong data'}, 400
        try:
            actor = Actor(
                first_name=actor_json['first_name'],
                last_name=actor_json['last_name'],
                description=actor_json.get('description')
            )
            db.session.add(actor)
            db.session.commit()
        except(ValueError, KeyError):
            return {'message': 'Wrong data'}, 400
        return {'message': 'Created successfully', 'uuid': actor.uuid}, 201

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass


api.add_resource(Smoke, '/smoke', strict_slashes=False)
api.add_resource(FilmListApi, '/films', '/films/<uuid>', strict_slashes=False)
api.add_resource(ActorListApi, '/actors', '/actors/<uuid>', strict_slashes=False)
