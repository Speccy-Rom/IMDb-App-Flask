import datetime

from aiopg.sa import create_engine
from sanic import Sanic, response
from sanic.views import HTTPMethodView
from sqlalchemy import select

import config
from src.database.models import Film

app = Sanic(__name__)


class AsyncFilmService:
    @classmethod
    async def fetch_all_films(cls):
        async with create_engine(config.Config.HEROKU_DATABASE_URI) as engine:
            async with engine.acquire() as conn:
                query = select([Film])
                result = await conn.execute(query)
                films = []
                async for row in result:
                    films.append(dict(row))
        return films


class FilmListApi(HTTPMethodView):
    async def get(self, request):
        films = await AsyncFilmService.fetch_all_films()
        for f in films:
            f['release_date'] = datetime.datetime.strftime(f['release_date'], '%Y-%m-%d')
        return response.json(films)


class Smoke(HTTPMethodView):
    async def get(self, request):
        return response.json(
            {'hello': 'world'}
        )


app.add_route(Smoke.as_view(), '/smoke')
app.add_route(FilmListApi.as_view(), '/films')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True, workers=4)