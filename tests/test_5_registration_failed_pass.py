from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators

def test_go_to_personal_account(driver):
    # переход по кнопке "Войти в аккаунт"
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((Locators.LOGIN_BUTTON_MAIN))).click()
    # переход по ссылке "зарегистрироваться"
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((Locators.REGISTER_LINK))).click()

    #Выполни авторизацию
    name_form = driver.find_element(*Locators.NAME_INPUT)
    name_form.clear()
    name_form.send_keys("TestName")

    mail_form = driver.find_element(*Locators.EMAIL_INPUT)
    mail_form.clear()
    mail_form.send_keys("testtestov5299@yandex.ru")

    password_form = driver.find_element(*Locators.PASSWORD_INPUT)
    password_form.clear()
    password_form.send_keys("12345") # вводим короткий пароль до 6 символов

    driver.find_element(*Locators.REGISTER_BUTTON).click()

    # Ждем появления сообщения об ошибке
    error_message = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((Locators.ERROR_MESSAGE))
    )

    # Проверяем текст ошибки
    assert error_message.text == "Некорректный пароль"
    print("✅ Тест завершен!")