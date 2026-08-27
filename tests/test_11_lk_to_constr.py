from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators

def test_go_to_personal_account(driver):
  # переход по кнопке "Личный кабинет"
  WebDriverWait(driver, 3).until(EC.element_to_be_clickable((Locators.PERSONAL_ACCOUNT_BUTTON))).click()
  # переход по кнопке "Конструктор"
  WebDriverWait(driver, 3).until(EC.element_to_be_clickable((Locators.CONSTRUCTOR_BUTTON))).click()
  print("✅ Тест пройден")