import os

import pytest
import os

from client import Client

@pytest.fixture(scope="session")
def client():
    return Client()

def get_test_data():
    test_data=os.environ.get("TEST_DATA")
    return test_data

