import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_type", action="store", default="chrome", help="The default value is chrome"
    )

@pytest.fixture(scope = "class")
def form_config_setup(request):

    browser = request.config.getoption("--browser_type")

    if browser == "chrome":
        Service_Object = Service()
        driver = webdriver.Chrome(service=Service_Object)
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
        request.cls.driver = driver

        yield
        driver.close()

    elif browser == "firefox":
        Service_Object = Service()
        driver = webdriver.Firefox(service=Service_Object)
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
        request.cls.driver = driver

        yield
        driver.close()

    elif browser == "ie":
        Service_Object = Service()
        driver = webdriver.Ie(service=Service_Object)
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
        request.cls.driver = driver

        yield
        driver.close()