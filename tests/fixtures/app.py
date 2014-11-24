import pytest
from gaia import create_app

@pytest.yield_fixture(autouse=True)
def client():
    """application with context."""
    app = create_app()
    ctx = app.app_context()
    ctx.push()
    yield app.test_client()
    ctx.pop()