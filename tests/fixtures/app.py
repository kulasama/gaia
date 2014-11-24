import pytest
from gaia import create_app
import json

@pytest.yield_fixture(autouse=True)
def client():
    """application with context."""
    app = create_app()
    ctx = app.app_context()
    ctx.push()
    yield app.test_client()
    ctx.pop()




class GAIA(object):

	def __init__(self,client):
		self.client = client

	def call(self,method,**params):
		payload = {
			"method":method,
			"params":json.dumps(params)
		}
		r = self.client.post("/api/",data = payload)
		return json.loads(r.data)

@pytest.yield_fixture(autouse=True)
def gaia():
    """application with context."""
    app = create_app()
    ctx = app.app_context()
    ctx.push()
    client = app.test_client()
    yield GAIA(client)
    ctx.pop()