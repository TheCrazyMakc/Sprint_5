from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators

def test_go_to_personal_account(driver):
  # переход по кнопке "Личный кабинет"
  WebDriverWait(driver, 3).until(EC.element_to_be_clickable((Locators.PERSONAL_ACCOUNT_BUTTON))).click()

  #Выполни авторизацию
  mail_form = driver.find_element(*Locators.EMAIL_INPUT)
  mail_form.clear()
  mail_form.send_keys("testtestov5299@yandex.ru")

  password_form = driver.find_element(*Locators.PASSWORD_INPUT)
  password_form.clear()
  password_form.send_keys("Qwerty123")

  driver.find_element(*Locators.LOGIN_BUTTON).click()
  print("✅ Тест пройден: Успешный вход")