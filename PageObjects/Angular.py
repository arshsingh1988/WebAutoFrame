from selenium.webdriver.common.by import By


class Angular:
    def __init__(self, driver):
        self.driver = driver

    Name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    radioButton = (By.ID, "inlineRadio1")
    submitButton = (By.XPATH, "//button[contains(text(),'Submit')]")

    def sendName(self):
        return self.driver.find_element(*Angular.Name)

    def sendEmail(self):
        return self.driver.find_element(*Angular.email)

    def sendPassword(self):
        return self.driver.find_element(*Angular.password)

    def clickCheckBox(self):
        return self.driver.find_element(*Angular.checkbox)

    def clickRadioButton(self):
        return self.driver.find_element(*Angular.radioButton)

    def clickSubmitButton(self):
        return self.driver.find_element(*Angular.submitButton)




