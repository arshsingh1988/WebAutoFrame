import pytest

from PageObjects.HomePage import HomePage
from PageObjects.SwitchWindows import SwitchWindows
from utils.BaseClass import BaseClass


class TestLanding(BaseClass):

    def test_pageValidation(self):
        homepage = HomePage(self.driver)
        homepage.logoButton().is_displayed()
        homepage.homeButton().is_displayed()
        homepage.practiceButton().is_displayed()
        homepage.loginButton().is_displayed()
        homepage.signupButton().is_displayed()

    def test_WindowButton(self):
        windows = SwitchWindows(self.driver)
        assert windows.switchWin().text
