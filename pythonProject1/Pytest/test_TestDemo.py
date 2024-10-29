import pytest

@pytest.mark.usefixtures("setUp")
class TestExample:

    def test_Method1(self):
        print("This is test method1")

    def test_Method2(self):
        print("This is test method2")
