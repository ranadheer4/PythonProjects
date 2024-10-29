import pytest

from Pytest.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class Testex(BaseClass):
    def test_editProfile(self,dataLoad):
        log=self.getLogger()
        log.info(dataLoad)
        print(dataLoad)
        print(dataLoad[0:])
        print(dataLoad[2])

def test_crossbrow(crossBrowser):
    print(crossBrowser[1])

