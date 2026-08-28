from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators

def test_go_to_personal_account(driver):
  # переход по кнопке "Войти в аккаунт"
  WebDriverWait(driver, 3).until(EC.element_to_be_clickable((Locators.LOGIN_BUTTON_MAIN))).click()
  # переход по ссылке "зарегистрироваться"
  WebDriverWait(driver, 3).until(EC.element_to_be_clickable((Locators.REGISTER_LINK))).click()

  # Запоминаем текущий URL до клика
  current_url_before = driver.current_url

  #Выполни авторизацию
  name_form = driver.find_element(*Locators.NAME_INPUT)
  name_form.clear()
  name_form.send_keys("") # вводим пустое значение

  mail_form = driver.find_element(*Locators.EMAIL_INPUT)
  mail_form.clear()
  mail_form.send_keys("testtestov52002@yandex.ru")

  password_form = driver.find_element(*Locators.PASSWORD_INPUT)
  password_form.clear()
  password_form.send_keys("Qwerty123")

  driver.find_element(*Locators.REGISTER_BUTTON).click()

  # Проверяем, что URL не изменился
  current_url_after = driver.current_url
  assert current_url_before == current_url_after, "Страница изменилась при пустом имени!"