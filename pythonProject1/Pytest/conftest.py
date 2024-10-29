import pytest


@pytest.fixture(scope="class")
def setUp():
    print("I'm exectue first")
    yield
    print("i will execute last")

@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Rahul", "Shetty", "dranadheer4@gmail.com"]

@pytest.fixture(params=[("chrome","rahul","shetty"),("Firefox","shetty"),("IE","SS")])
def crossBrowser(request):
    return request.param
