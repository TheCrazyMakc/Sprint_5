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
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
        ), "Кнопка 'Личный кабинет' не появилась!"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

    @pytest.mark.navigation
    def test_go_to_constructor_from_lk(self, driver):
        """Переход из личного кабинета в конструктор"""
        # Переход в ЛК
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
        ), "Кнопка 'Личный кабинет' не появилась!"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Переход в конструктор
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)
        ), "Кнопка 'Конструктор' не появилась!"
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        
        # Проверка, что на главной
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
        ), "Кнопка 'Войти в аккаунт' не появилась на главной!"

    @pytest.mark.navigation
    def test_go_to_main_from_lk(self, driver):
        """Переход на главную через логотип"""
        # Переход в ЛК
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
        ), "Кнопка 'Личный кабинет' не появилась!"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Клик по логотипу
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGO_BUTTON)
        ), "Логотип не появился!"
        driver.find_element(*Locators.LOGO_BUTTON).click()
        
        # Проверка, что на главной
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
        ), "Кнопка 'Войти в аккаунт' не появилась на главной!"

    @pytest.mark.navigation
    def test_exit_from_lk(self, driver):
        """Выход из личного кабинета"""
        # Вход
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
        
        # Проверка успешного входа
        assert WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)
        ), "Кнопка 'Конструктор' не появилась после входа!"
        
        # Переход в ЛК
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
        ), "Кнопка 'Личный кабинет' не появилась!"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Выход
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.EXIT_BUTTON)
        ), "Кнопка 'Выход' не появилась!"
        driver.find_element(*Locators.EXIT_BUTTON).click()
        
        # Проверка, что вышли
        assert WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON)
        ), "Кнопка 'Войти' не появилась после выхода!"