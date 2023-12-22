from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    logo = (By.CSS_SELECTOR, "img[class = 'logoClass']")

    def logoButton(self):
        return self.driver.find_element(*HomePage.logo)

    home = (By.XPATH, "//button[text()[contains(.,'Home')]]")

    def homeButton(self):
        return self.driver.find_element(*HomePage.home)

    practice = (By.XPATH, "//button[contains(text(),'Practice')]")

    def practiceButton(self):
        return self.driver.find_element(*HomePage.practice)

    login = (By.XPATH, "//button[contains(text(),'Login')]")

    def loginButton(self):
        return self.driver.find_element(*HomePage.logo)

    signup = (By.XPATH, "//button[contains(text(),'Signup')]")

    def signupButton(self):
        return self.driver.find_element(*HomePage.signup)




