import pytest


@pytest.fixture()
def test_setup():
    print("I will be execute first")
    yield
    print("I will execute last")

def test_fixtureDemo(test_setup):
    print("I'll be execute steps in fixturedemo method")