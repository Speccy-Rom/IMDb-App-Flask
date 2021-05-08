from typing import List

from flask import request
from flask_restful import Resource

from src import api


class Smoke(Resource):
    def get(self):
        return {'message': 'OK'}, 200


def get_all_films():
    return [
        {
            'id': '1',
            'title': 'Harry Potter and the Philosopher\'s Stone',
            'release_date': 2001
        },
        {
            'id': '2',
            'title': 'Harry Potter and the Chamber of Secrets',
            'release_date': 2002
        },
        {
            'id': '3',
            'title': 'Harry Potter and the Prisoner of Azkaban',
            'release_date': 2004
        },
        {
            'id': '4',
            'title': 'Harry Potter and the Goblet of Fire',
            'release_date': 2005
        },
        {
            'id': '5',
            'title': 'Harry Potter and the Order of the Phoenix',
            'release_date': 2007
        },
        {
            'id': '6',
            'title': 'Harry Potter and the Half-Blood Prince',
            'release_date': 2009
        },
        {
            'id': '7',
            'title': 'Harry Potter and the Deathly Hallows. Part 1',
            'release_date': 2010
        },
        {
            'id': '8',
            'title': 'Harry Potter and the Deathly Hallows. Part 2',
            'release_date': 2011
        },
    ]


def get_film_by_uuid(uuid: str) -> dict:
    films = get_all_films()
    film = list(filter(lambda f: f['id'] == uuid, films))
    return films[0] if film else {}


def create_film(film_json: dict) -> List[dict]:
    films = get_all_films()
    films.append(film_json)
    return films


class FilmListApi(Resource):
    def get(self, uuid=None):
        if not uuid:
            films = get_all_films()
            return films, 200
        film = get_film_by_uuid(uuid)
        if not film:
            return '', 404
        return film, 200

    def post(self):
        film_json = request.json
        return create_film(film_json), 201

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass


class ActorListApi(Resource):
    def get(self, uuid=None):
        if not uuid:
            pass
        pass

    def post(self):
        pass

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass


api.add_resource(Smoke, '/smoke', strict_slashes=False)
api.add_resource(FilmListApi, '/films', '/films/<uuid>', strict_slashes=False)
