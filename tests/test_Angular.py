import pytest

from PageObjects.Angular import Angular
from utils.BaseClass import BaseClass
from TestData.HomePageTestData import HomePageTestData


class TestAngular(BaseClass):
    @pytest.mark.skip
    def test_SubmitForm(self, getData):
        angularPage = Angular(self.driver)
        log = self.getLogger()
        log.info("Test Started")
        angularPage.sendName().send_keys(getData["Name"])
        angularPage.sendEmail().send_keys(getData["Email"])
        angularPage.sendPassword().send_keys(getData["Password"])
        log.info("Test End")
        self.driver.refresh()

    @pytest.mark.skip
    @pytest.fixture(params=HomePageTestData.test_homepage_data)
    def getData(self, request):
        return request.param
