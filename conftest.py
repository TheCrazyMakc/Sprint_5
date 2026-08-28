import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


@pytest.fixture
def driver():
    """Фикстура для создания и закрытия драйвера"""
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/")
    yield driver
    driver.quit()