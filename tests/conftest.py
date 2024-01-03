import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


LandingURL = "https://rahulshettyacademy.com/AutomationPractice/"
LandingURL1 = "https://rahulshettyacademy.com/angularpractice/"
expedia_Url = "https://www.expedia.com/"


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    #parser.addoption("--env_name", action="store", default="https://rahulshettyacademy.com/angularpractice/")


@pytest.fixture(scope="class")
def setup(request):
    serv = Service()
    browser_name = request.config.getoption("--browser_name")
    #env = request.config.getoption("--env_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=serv)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=serv)
    elif browser_name == "IE":   # this is not working right now.
        driver = webdriver.ie
    elif browser_name == "safari":
        driver = webdriver.Safari()
    driver.get(expedia_Url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
