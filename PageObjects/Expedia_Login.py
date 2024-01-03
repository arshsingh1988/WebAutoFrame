from selenium.webdriver.common.by import By


class Expedia_Login:
    def __init__(self, driver):
        self.driver = driver

    Login = (By.XPATH, "//button[contains(text(),'Sign in')]")
    Login_Banner = (By.PARTIAL_LINK_TEXT, "//a[text()= 'Sign in, it']")
    ExpediaRewardText= (By.LINK_TEXT, "")
    SignInText = (By.XPATH, "//h1[contains(text(),'Sign in or create an account')]")
    GoogleTitle = (By.ID, "social-auth-provider-google-web")
    EmailTextBox = (By.ID, "loginFormEmailInput")
    EnterEmailText = (By.ID, "loginFormEmailInput-error")
    ContinueButton = (By.ID, "loginFormSubmitButton")
    PasswordButtonInstead = (By.ID, "passwordButton")
    PasswordInput = (By.ID, "enterPasswordFormPasswordInput")
    SignInButton = (By.ID, "enterPasswordFormSubmitButton")
    UserName = (By.XPATH, "//button[contains(text(),'Arsh')]")
    SignOut = (By.XPATH, "//a[@aria-label ='Sign out']")
    Stays = (By.XPATH, "//span[text()='Stays']")
    Flights = (By.XPATH, "//span[text()='Flights']")
    Cars = (By.XPATH, "//span[text()='Cars']")
    Packages = (By.XPATH, "//span[text()='Packages']")
    ThingsToDo = (By.XPATH, "//span[text()='Things to do']")
    Cruises = (By.XPATH, "//span[text()='Cruises']")

    def LoginButton(self):
        return self.driver.find_element(*Expedia_Login.Login)

    def LoginBanner(self):
        return self.driver.find_element(*Expedia_Login.Login_Banner)

    def SignInWord(self):
        return self.driver.find_element(*Expedia_Login.SignInText)

    def GoogleButton(self):
        return self.driver.find_element(*Expedia_Login.GoogleTitle)

    def EmailErrorText(self):
        return self.driver.find_element(*Expedia_Login.EnterEmailText)

    def EmailText(self):
        return self.driver.find_element(*Expedia_Login.EmailTextBox)

    def ContinueBtn(self):
        return self.driver.find_element(*Expedia_Login.ContinueButton)

    def StayTab(self):
        return self.driver.find_element(*Expedia_Login.Stays)

    def FlightTab(self):
        return self.driver.find_element(*Expedia_Login.Flights)

    def CarsTab(self):
        return self.driver.find_element(*Expedia_Login.Cars)

    def PackageTab(self):
        return self.driver.find_element(*Expedia_Login.Packages)

    def ThingsToDoTab(self):
        return self.driver.find_element(*Expedia_Login.ThingsToDo)

    def CruisesTab(self):
        return self.driver.find_element(*Expedia_Login.Cruises)






