import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestMenu:
    """Класс для тестов меню продуктов"""
    
    @pytest.mark.menu
    def test_food_menu_sections(self, driver):
        """Переходы по разделам меню"""
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

        # Проверка пунктов меню
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((Locators.SAUCES_TAB))).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((Locators.FILLINGS_TAB))).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((Locators.BUNS_TAB))).click()

        # Проверка разделов меню
        # WebDriverWait(driver, 3).until(
        #     EC.element_to_be_clickable(Locators.SAUCES_TAB)
        # ).click()
        # WebDriverWait(driver, 3).until(
        #     EC.visibility_of_element_located(Locators.SAUCES_SECTION)
        # )
        # print("✅ Раздел 'Соусы'")

        # WebDriverWait(driver, 3).until(
        #     EC.element_to_be_clickable(Locators.FILLINGS_TAB)
        # ).click()
        # WebDriverWait(driver, 3).until(
        #     EC.visibility_of_element_located(Locators.FILLINGS_SECTION)
        # )
        # print("✅ Раздел 'Начинки'")

        # WebDriverWait(driver, 3).until(
        #     EC.element_to_be_clickable(Locators.BUNS_TAB)
        # ).click()
        # WebDriverWait(driver, 3).until(
        #     EC.visibility_of_element_located(Locators.BUNS_SECTION)
        # )