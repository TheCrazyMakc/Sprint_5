import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import Locators
from urls import Urls
from helpers import generate_unique_email, generate_password
from selenium.common.exceptions import TimeoutException


class TestRegistration:
    """Класс для всех тестов регистрации"""
    
    @pytest.mark.registration
    def test_successful_registration(self, driver):
        """Успешная регистрация с уникальными данными"""
        unique_email = generate_unique_email()
        unique_password = generate_password(6)
        
        # Переход на страницу регистрации
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
        ), "Кнопка 'Войти в аккаунт' не появилась!"
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        ), "Ссылка 'Зарегистрироваться' не появилась!"
        driver.find_element(*Locators.REGISTER_LINK).click()

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

        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.REGISTER_BUTTON)
        ), "Кнопка 'Зарегистрироваться' не появилась!"
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Проверка успешной регистрации
        assert WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON)
        ), "Кнопка 'Войти' не появилась после регистрации!"

    @pytest.mark.registration
    def test_registration_with_existing_email(self, driver):
        """Регистрация с уже существующим email"""
        # переход на страницу регистрации
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
        ), "Кнопка 'Войти в аккаунт' не появилась!"
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        ), "Ссылка 'Зарегистрироваться' не появилась!"
        driver.find_element(*Locators.REGISTER_LINK).click()

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

        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.REGISTER_BUTTON)
        ), "Кнопка 'Зарегистрироваться' не появилась!"
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        try:
            error_element = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'input__error') and contains(text(), 'Такой пользователь уже существует')]"))
            )
            assert error_element.is_displayed(), "Элемент ошибки не отображается!"
        except TimeoutException:
            # Если ошибка не появилась, проверяем, что мы на странице регистрации
            assert "register" in driver.current_url, "Ошибка не появилась, но и регистрация не прошла!"
            assert False, "Сообщение об ошибке 'Такой пользователь уже существует' не появилось!"

    @pytest.mark.registration
    def test_registration_with_empty_name(self, driver):
        """Регистрация с пустым именем"""
        # переход на страницу регистрации
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
        ), "Кнопка 'Войти в аккаунт' не появилась!"
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        ), "Ссылка 'Зарегистрироваться' не появилась!"
        driver.find_element(*Locators.REGISTER_LINK).click()

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

        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.REGISTER_BUTTON)
        ), "Кнопка 'Зарегистрироваться' не появилась!"
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Проверка, что URL не изменился
        current_url_after = driver.current_url
        assert current_url_before == current_url_after, "URL изменился при пустом имени!"


    @pytest.mark.registration
    def test_registration_with_invalid_email(self, driver):
        """Регистрация с неверным email"""
        # переход на страницу регистрации
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
        ), "Кнопка 'Войти в аккаунт' не появилась!"
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        ), "Ссылка 'Зарегистрироваться' не появилась!"
        driver.find_element(*Locators.REGISTER_LINK).click()

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

        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.REGISTER_BUTTON)
        ), "Кнопка 'Зарегистрироваться' не появилась!"
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        try:
            error_element = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'input__error') and contains(text(), 'Такой пользователь уже существует')]"))
            )
            assert error_element.is_displayed(), "Элемент ошибки не отображается!"
        except TimeoutException:
            # Если ошибка не появилась, проверяем, что мы на странице регистрации
            assert "register" in driver.current_url, "Ошибка не появилась, но и регистрация не прошла!"
            assert False, "Сообщение об ошибке 'Такой пользователь уже существует' не появилось!"

    @pytest.mark.registration
    def test_registration_with_short_password(self, driver):
        """Регистрация с коротким паролем (< 6 символов)"""
        # переход на страницу регистрации
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN)
        ), "Кнопка 'Войти в аккаунт' не появилась!"
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        ), "Ссылка 'Зарегистрироваться' не появилась!"
        driver.find_element(*Locators.REGISTER_LINK).click()

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

        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.REGISTER_BUTTON)
        ), "Кнопка 'Зарегистрироваться' не появилась!"
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        error_elements = driver.find_elements(By.XPATH, "//p[contains(@class, 'input__error') and contains(text(), 'Некорректный пароль')]")
        assert len(error_elements) > 0, "Сообщение об ошибке 'Некорректный пароль' не найдено!"
        assert error_elements[0].is_displayed(), "Элемент ошибки не отображается!"