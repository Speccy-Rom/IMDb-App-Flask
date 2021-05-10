from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from src import db
from src.database.models import Actor
from src.schemas.actors import ActorSchema


class ActorListApi(Resource):
    actor_schema = ActorSchema()

    def get(self, name=None):
        if not name:
            actors = db.session.query(Actor).all()
            return self.actor_schema.dump(actors, many=True), 200
        actor = db.session.query(Actor).filter_by(name=name).first()
        if not actor:
            return '', 404
        return self.actor_schema.dump(actor), 200

    def post(self):
        try:
            actor = self.actor_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return{'message': str(e)}, 400
        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 201

    def put(self, name):
        actor = db.session.query(Actor).filter_by(name=name).first()
        if not actor:
            return "", 404
        try:
            actor = self.actor_schema.load(request.json, instance=actor, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 200

    def patch(self, name):
        pass
        # actor = db.session.query(Actor).filter_by(uuid=uuid).first()
        # if not actor:
        #     return "", 404
        # try:
        #     actor = self.actor_schema.load(request.json, instance=actor, session=db.session)
        # except ValidationError as e:
        #     return {'message': str(e)}, 400
        # actor_json = request.json
        # name = actor_json.get('name')
        # birthday = actor_json.get('birthday')
        # is_active = actor_json.get('is_active')
        # if name:
        #     actor.name = name
        # elif birthday:
        #     actor.birthday = birthday
        # elif is_active:
        #     actor.is_active = is_active
        #
        # db.session.add(actor)
        # db.session.commit()
        # return {'message': 'Updated successfully'}, 200

    def delete(self, name):
        actor = db.session.query(Actor).filter_by(name=name).first()
        if not actor:
            return "", 404
        db.session.delete(actor)
        db.session.commit()
        return '', 204
