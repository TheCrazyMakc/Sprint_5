import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from urls import Urls


class TestNavigation:
    """Класс для всех тестов навигации"""
    
    @pytest.mark.navigation
    def test_go_to_personal_account(self, driver):
        """Переход в личный кабинет"""
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
        ).click()

    @pytest.mark.navigation
    def test_go_to_constructor_from_lk(self, driver):
        """Переход из личного кабинета в конструктор"""
        # Переход в ЛК
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        # Переход в конструктор
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)
        ).click()
        
        # Проверка, что на главной
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
        )

    @pytest.mark.navigation
    def test_go_to_main_from_lk(self, driver):
        """Переход на главную через логотип"""
        # Переход в ЛК
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        # Клик по логотипу
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGO_BUTTON)
        ).click()
        
        # Проверка, что на главной
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
        )

    @pytest.mark.navigation
    def test_exit_from_lk(self, driver):
        """Выход из личного кабинета"""
        # Вход
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
        
        # Переход в ЛК
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
        ).click()
        
        # Выход
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.EXIT_BUTTON)
        ).click()
        
        # Проверка, что вышли
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON)
        )