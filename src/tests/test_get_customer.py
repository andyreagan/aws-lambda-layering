import pytest

from .conftest import test_client as client

URL = "/customer/blah"


@pytest.mark.django_db(transaction=True)
@pytest.mark.usefixtures("default_customer")
class TestGetCustomer:
    @staticmethod
    def test_get_customer():
        response = client.get(URL)
        assert response.status_code == 200
