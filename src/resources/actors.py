from flask import request
from flask_restful import Resource

from src import db
from src.database.models import Actor
from src.schemas.actors import ActorSchema


class ActorListApi(Resource):
    actor_schema = ActorSchema()

    def get(self, uuid=None):
        if not uuid:
            actors = db.session.query(Actor).all()
            return self.actor_schema.dump(actors, many=True), 200
        actor = db.session.query(Actor).filter_by(uuid=uuid).first()
        if not actor:
            return '', 404
        return self.actor_schema.dump(actor), 200

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

    def put(self, uuid):
        actor_json = request.json
        if not actor_json:
            return {'message': 'Wrong data'}, 400
        try:
            db.session.querty(Actor).filter_by(uuid=uuid).update(
                dict(
                    first_name=actor_json['first_name'],
                    last_name=actor_json['last_name'],
                    description=actor_json.get('description')
                )
            )
            db.session.commit()
        except (ValueError, KeyError):
            return {'message': 'Wrong data'}, 400
        return {'message': 'Updated successfully'}, 200

    def patch(self, uuid):
        actor = db.session.query(Actor).filter_by(uuid=uuid).first()
        if not actor:
            return "", 404
        actor_json = request.json
        first_name = actor_json.get('first_name')
        last_name = actor_json.get('last_name')
        description = actor_json.get('description')
        if first_name:
            actor.first_name = first_name
        elif last_name:
            actor.last_name = last_name
        elif description:
            actor.description = description

        db.session.add(actor)
        db.session.commit()
        return {'message': 'Updated successfully'}, 200

    def delete(self, uuid):
        actor = db.session.query(Actor).filter_by(uuid=uuid).first()
        if not actor:
            return "", 404
        db.session.delete(actor)
        db.session.commit()
        return '', 204
