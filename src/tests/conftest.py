import pytest
from app import app
from fastapi.testclient import TestClient
from pytest import fixture

from db.models import Customer

test_client = TestClient(app)
app.user_middleware.clear()
app.middleware_stack = app.build_middleware_stack()

MOCKED_USER = {
    "user_id": "blah",
}


@fixture
@pytest.mark.django_db
def default_customer():
    yield Customer.objects.create(customerId=MOCKED_USER["user_id"])
