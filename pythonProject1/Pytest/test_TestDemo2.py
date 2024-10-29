import pytest
@pytest.mark.xfail
def test_Man():
    msg="Hello"
    assert msg=="Hpy", "Strings not matches"

