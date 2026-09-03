import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestLogin:
    """Класс для всех тестов входа"""
    
    @pytest.mark.login
    def test_login_from_main(self, driver):
        """Вход через кнопку на главной странице"""
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
        ), "Кнопка 'Войти в аккаунт' не появилась!"
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()

        mail_form = driver.find_element(*Locators.EMAIL_INPUT)
        mail_form.clear()
        mail_form.send_keys("testtestov5299@yandex.ru")

        password_form = driver.find_element(*Locators.PASSWORD_INPUT)
        password_form.clear()
        password_form.send_keys("Qwerty123")

        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON)
        ), "Кнопка 'Войти' не появилась!"
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)
        ), "Кнопка 'Конструктор' не появилась после входа!"

    @pytest.mark.login
    def test_login_from_personal_account(self, driver):
        """Вход через кнопку 'Личный кабинет'"""
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
        ), "Кнопка 'Личный кабинет' не появилась!"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        mail_form = driver.find_element(*Locators.EMAIL_INPUT)
        mail_form.clear()
        mail_form.send_keys("testtestov5299@yandex.ru")

        password_form = driver.find_element(*Locators.PASSWORD_INPUT)
        password_form.clear()
        password_form.send_keys("Qwerty123")

        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON)
        ), "Кнопка 'Войти' не появилась!"
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)
        ), "Кнопка 'Конструктор' не появилась после входа!"

    @pytest.mark.login
    def test_login_from_registration_form(self, driver):
        """Вход через форму регистрации"""
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
        ), "Кнопка 'Войти в аккаунт' не появилась!"
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        ), "Ссылка 'Зарегистрироваться' не появилась!"
        driver.find_element(*Locators.REGISTER_LINK).click()
        
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_LINK_ON_REGISTER)
        ), "Ссылка 'Войти' не появилась!"
        driver.find_element(*Locators.LOGIN_LINK_ON_REGISTER).click()

        mail_form = driver.find_element(*Locators.EMAIL_INPUT)
        mail_form.clear()
        mail_form.send_keys("testtestov5299@yandex.ru")

        password_form = driver.find_element(*Locators.PASSWORD_INPUT)
        password_form.clear()
        password_form.send_keys("Qwerty123")

        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON)
        ), "Кнопка 'Войти' не появилась!"
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)
        ), "Кнопка 'Конструктор' не появилась после входа!"

    @pytest.mark.login
    def test_login_from_forgot_password(self, driver):
        """Вход через форму восстановления пароля"""
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
        ), "Кнопка 'Войти в аккаунт' не появилась!"
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.FORGOT_PASSWORD_LINK)
        ), "Ссылка 'Восстановить пароль' не появилась!"
        driver.find_element(*Locators.FORGOT_PASSWORD_LINK).click()
        
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_LINK_ON_REGISTER)
        ), "Ссылка 'Войти' не появилась!"
        driver.find_element(*Locators.LOGIN_LINK_ON_REGISTER).click()

        mail_form = driver.find_element(*Locators.EMAIL_INPUT)
        mail_form.clear()
        mail_form.send_keys("testtestov5299@yandex.ru")

        password_form = driver.find_element(*Locators.PASSWORD_INPUT)
        password_form.clear()
        password_form.send_keys("Qwerty123")

        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON)
        ), "Кнопка 'Войти' не появилась!"
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        
        assert WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)
        ), "Кнопка 'Конструктор' не появилась после входа!"