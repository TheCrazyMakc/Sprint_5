import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestMenu:
    """Класс для тестов меню продуктов"""
    
    @pytest.mark.menu
    def test_sauces_tab_active(self, driver):
        """Проверка, что при клике на 'Соусы' добавляется активный класс"""
        # Клик на таб "Соусы"
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.SAUCES_TAB)
        ), "Таб 'Соусы' не появился!"
        driver.find_element(*Locators.SAUCES_TAB).click()

        # Проверяем, что добавился класс активности
        sauces_tab = driver.find_element(*Locators.SAUCES_TAB)
        class_attribute = sauces_tab.get_attribute("class")
        assert "tab_tab_type_current__2BEPc" in class_attribute, f"Класс активности не добавлен для таба 'Соусы'. Класс: {class_attribute}"

    @pytest.mark.menu
    def test_fillings_tab_active(self, driver):
        """Проверка, что при клике на 'Начинки' добавляется активный класс"""
        # Клик на таб "Начинки"
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.FILLINGS_TAB)
        ), "Таб 'Начинки' не появился!"
        driver.find_element(*Locators.FILLINGS_TAB).click()

        # Проверяем, что добавился класс активности
        fillings_tab = driver.find_element(*Locators.FILLINGS_TAB)
        class_attribute = fillings_tab.get_attribute("class")
        assert "tab_tab_type_current__2BEPc" in class_attribute, f"Класс активности не добавлен для таба 'Начинки'. Класс: {class_attribute}"

    @pytest.mark.menu
    def test_buns_tab_active(self, driver):
        """Проверка, что при клике на 'Булки' добавляется активный класс"""
        # Сначала кликаем на другой таб (чтобы снять активность с "Булок")
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.SAUCES_TAB)
        ), "Таб 'Соусы' не появился!"
        driver.find_element(*Locators.SAUCES_TAB).click()

        # Клик на таб "Булки"
        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(Locators.BUNS_TAB)
        ), "Таб 'Булки' не появился!"
        driver.find_element(*Locators.BUNS_TAB).click()

        # Проверяем, что добавился класс активности
        buns_tab = driver.find_element(*Locators.BUNS_TAB)
        class_attribute = buns_tab.get_attribute("class")
        assert "tab_tab_type_current__2BEPc" in class_attribute, f"Класс активности не добавлен для таба 'Булки'. Класс: {class_attribute}"