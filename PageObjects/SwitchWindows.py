from selenium.webdriver.common.by import By


class SwitchWindows:
    def __init__(self, driver):
        self.driver = driver

    switch = (By.ID, "openwindow")

    def switchWin(self):
        return self.driver.find_element(*SwitchWindows.switch)
