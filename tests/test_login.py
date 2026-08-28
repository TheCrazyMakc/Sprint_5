import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestLogin:
    """Класс для всех тестов входа"""
    
    @pytest.mark.login
    def test_login_from_main(self, driver):
        """Вход через кнопку на главной странице"""
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
        ).click()

        mail_form = driver.find_element(*Locators.EMAIL_INPUT)
        mail_form.clear()
        mail_form.send_keys("testtestov5299@yandex.ru")

        password_form = driver.find_element(*Locators.PASSWORD_INPUT)
        password_form.clear()
        password_form.send_keys("Qwerty123")

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        
        # Проверка успешного входа
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)
        )

    @pytest.mark.login
    def test_login_from_personal_account(self, driver):
        """Вход через кнопку 'Личный кабинет'"""
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
        ).click()

        mail_form = driver.find_element(*Locators.EMAIL_INPUT)
        mail_form.clear()
        mail_form.send_keys("testtestov5299@yandex.ru")

        password_form = driver.find_element(*Locators.PASSWORD_INPUT)
        password_form.clear()
        password_form.send_keys("Qwerty123")

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        
        # Проверка успешного входа
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)
        )

    @pytest.mark.login
    def test_login_from_registration_form(self, driver):
        """Вход через форму регистрации"""
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
        ).click()
        
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        ).click()
        
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_LINK_ON_REGISTER)
        ).click()

        mail_form = driver.find_element(*Locators.EMAIL_INPUT)
        mail_form.clear()
        mail_form.send_keys("testtestov5299@yandex.ru")

        password_form = driver.find_element(*Locators.PASSWORD_INPUT)
        password_form.clear()
        password_form.send_keys("Qwerty123")

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        
        # Проверка успешного входа
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)
        )

    @pytest.mark.login
    def test_login_from_forgot_password(self, driver):
        """Вход через форму восстановления пароля"""
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
        ).click()
        
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.FORGOT_PASSWORD_LINK)
        ).click()
        
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_LINK_ON_REGISTER)
        ).click()

        mail_form = driver.find_element(*Locators.EMAIL_INPUT)
        mail_form.clear()
        mail_form.send_keys("testtestov5299@yandex.ru")

        password_form = driver.find_element(*Locators.PASSWORD_INPUT)
        password_form.clear()
        password_form.send_keys("Qwerty123")

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        
        # Проверка успешного входа
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)
        )