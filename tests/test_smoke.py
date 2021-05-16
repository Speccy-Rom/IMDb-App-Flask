import http

from src import app


def test_smoke():
    client = app.test_client()
    resp = client.get('/smoke')
    assert resp.status_code == http.HTTPStatus.OK

#  pipenv install pytest --dev ##  для того что бы указать что pytest является не основной зависимостью проекта,
#  а для dev разработки

