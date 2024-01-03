import time

from utils.BaseClass import BaseClass
from PageObjects.Expedia_Login import Expedia_Login


class TestExpediaLogin(BaseClass):
    def test_ValidateElementsMainPage(self):
        Expedia_LoginTest = Expedia_Login(self.driver)
        log = self.getLogger()
        log.info("Test Started")
        if Expedia_LoginTest.LoginButton().is_displayed():
            log.info("Login button displayed")
        else:
            log.error("Login button is not showing.")
        if Expedia_LoginTest.StayTab() is True:
            log.info("Stays Tab displayed")
        else:
            log.error("Stays Tab is not showing")
        if Expedia_LoginTest.FlightTab() is True:
            log.info("Flight Tab displayed")
        else:
            log.error("Flight Tab is not showing")
        if Expedia_LoginTest.PackageTab() is True:
            log.info("Package Tab displayed")
        else:
            log.error("Package Tab is not showing")
        if Expedia_LoginTest.ThingsToDoTab() is True:
            log.info("Things to do Tab displayed")
        else:
            log.error("Things to do Tab is not showing")
        if Expedia_LoginTest.CarsTab() is True:
            log.info("Cruise Tab displayed")
        else:
            log.error("Cruise Tab is not showing")
        log.info("Test Finished")







