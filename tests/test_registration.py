import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from urls import Urls
from helpers import generate_unique_email, generate_password


class TestRegistration:
    """Класс для всех тестов регистрации"""
    
    @pytest.mark.registration
    def test_successful_registration(self, driver):
        """Успешная регистрация с уникальными данными"""
        unique_email = generate_unique_email()
        unique_password = generate_password(6)
        
        # Переход на страницу регистрации
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
        ).click()
        
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        ).click()

        # Заполнение формы
        name_form = driver.find_element(*Locators.NAME_INPUT)
        name_form.clear()
        name_form.send_keys("TestName")

        mail_form = driver.find_element(*Locators.EMAIL_INPUT)
        mail_form.clear()
        mail_form.send_keys(unique_email)

        password_form = driver.find_element(*Locators.PASSWORD_INPUT)
        password_form.clear()
        password_form.send_keys(unique_password)

        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Проверка успешной регистрации
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON)
        )

    @pytest.mark.registration
    def test_registration_with_existing_email(self, driver):
        """Регистрация с уже существующим email"""
        # переход на страницу регистрации
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
        ).click()
        
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        ).click()

        # Заполнение формы существующим email
        name_form = driver.find_element(*Locators.NAME_INPUT)
        name_form.clear()
        name_form.send_keys("TestName")

        mail_form = driver.find_element(*Locators.EMAIL_INPUT)
        mail_form.clear()
        mail_form.send_keys("testtestov5299@yandex.ru")

        password_form = driver.find_element(*Locators.PASSWORD_INPUT)
        password_form.clear()
        password_form.send_keys("Qwerty123")

        driver.find_element(*Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ERROR_MESSAGE))
        '''я не могу понять, как это нужно сделать по другому, прошу вас подсказать, как это сделать правильно'''

    @pytest.mark.registration
    def test_registration_with_empty_name(self, driver):
        """Регистрация с пустым именем"""
        # переход на страницу регистрации
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
        ).click()
        
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        ).click()

        current_url_before = driver.current_url

        # Заполнение формы с пустым именем
        name_form = driver.find_element(*Locators.NAME_INPUT)
        name_form.clear()
        name_form.send_keys("")

        mail_form = driver.find_element(*Locators.EMAIL_INPUT)
        mail_form.clear()
        mail_form.send_keys("testtestov52002@yandex.ru")

        password_form = driver.find_element(*Locators.PASSWORD_INPUT)
        password_form.clear()
        password_form.send_keys("Qwerty123")

        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Проверка, что URL не изменился
        current_url_after = driver.current_url
        assert current_url_before == current_url_after

    @pytest.mark.registration
    def test_registration_with_invalid_email(self, driver):
        """Регистрация с неверным email"""
        # переход на страницу регистрации
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
        ).click()
        
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        ).click()

        # Заполнение формы с неверным email
        name_form = driver.find_element(*Locators.NAME_INPUT)
        name_form.clear()
        name_form.send_keys("TestName")

        mail_form = driver.find_element(*Locators.EMAIL_INPUT)
        mail_form.clear()
        mail_form.send_keys("testtestov5299#yandex.ru")

        password_form = driver.find_element(*Locators.PASSWORD_INPUT)
        password_form.clear()
        password_form.send_keys("Qwerty123")

        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Ждем появления сообщения об ошибке
        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ERROR_MESSAGE))

        # Проверяем текст ошибки
        assert error_message.text == "Такой пользователь уже существует"

        '''Я не могу понять, как исправить этот код?
мы ждем появление сообщения об ошибке, она появляется только если мы ввели некорректный адрес:
error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ERROR_MESSAGE))

и далее проверяем текст этой ошибки, что она относится именно к проблеме с неверным адресом:
assert error_message.text == "Такой пользователь уже существует"

я не могу понять, как это нужно сделать по другому, прошу вас подсказать, как это сделать правильно'''

    @pytest.mark.registration
    def test_registration_with_short_password(self, driver):
        """Регистрация с коротким паролем (< 6 символов)"""
        # переход на страницу регистрации
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
        ).click()
        
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        ).click()

        # Заполнение формы с коротким паролем
        name_form = driver.find_element(*Locators.NAME_INPUT)
        name_form.clear()
        name_form.send_keys("TestName")

        mail_form = driver.find_element(*Locators.EMAIL_INPUT)
        mail_form.clear()
        mail_form.send_keys("testtestov5299@yandex.ru")

        password_form = driver.find_element(*Locators.PASSWORD_INPUT)
        password_form.clear()
        password_form.send_keys("12345")

        driver.find_element(*Locators.REGISTER_BUTTON).click()

        error_elements = driver.find_elements(*Locators.ERROR_MESSAGE)
        assert len(error_elements) > 0, "Сообщение об ошибке не найдено!"
        error_message = error_elements[0]
        assert error_message.text == "Некорректный пароль"