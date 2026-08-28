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

  WebDriverWait(driver, 10).until(
        EC.url_contains("stellarburgers")
    )

  WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((Locators.PERSONAL_ACCOUNT_BUTTON))
    ).click()

  WebDriverWait(driver, 10).until(
        EC.url_contains("/account/profile")
    )

  current_url = driver.current_url
  expected_url = "https://stellarburgers.education-services.ru/account/profile"
  assert current_url == expected_url, f"Ожидался URL '{expected_url}', а получен '{current_url}'"