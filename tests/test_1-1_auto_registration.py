import random
import string
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators


def generate_unique_email():
    """Генерирует уникальный email с случайным числом"""
    random_number = random.randint(100, 999)
    return f"testtestov52{random_number}@yandex.ru"

def generate_password(length=6):
    """Генерирует пароль заданной длины (по умолчанию 6 символов)"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def test_go_to_personal_account(driver):
    # Генерируем новый email перед каждым тестом
    unique_email = generate_unique_email()
    unique_password = generate_password(6)  # Генерируем пароль из 6 символов
    
    # переход по кнопке "Войти в аккаунт"
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((Locators.LOGIN_BUTTON_MAIN))
    ).click()
    
    # переход по ссылке "зарегистрироваться"
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((Locators.REGISTER_LINK))
    ).click()

    # Выполни авторизацию
    name_form = driver.find_element(*Locators.NAME_INPUT)
    name_form.clear()
    name_form.send_keys("TestName")

    mail_form = driver.find_element(*Locators.EMAIL_INPUT)
    mail_form.clear()
    mail_form.send_keys(unique_email)  # ← Используем сгенерированный email

    password_form = driver.find_element(*Locators.PASSWORD_INPUT)
    password_form.clear()
    password_form.send_keys(unique_password)

    driver.find_element(*Locators.REGISTER_BUTTON).click()

    # Проверяем, что регистрация успешная (появилась кнопка "Войти")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.LOGIN_BUTTON)
    )
    
    print("✅ Тест пройден: Успешная регистрация")