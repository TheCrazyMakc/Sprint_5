from selenium.webdriver.common.by import By


class Locators:
    # Кнопки
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[contains(., 'Войти в аккаунт')]")    
    REGISTER_BUTTON = (By.XPATH, "//button[contains(., 'Зарегистрироваться')]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(., 'Личный Кабинет')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(., 'Конструктор')]")
    LOGO_BUTTON = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2")
    EXIT_BUTTON = (By.XPATH, "//button[contains(., 'Выход')]")
    
    # Поля ввода
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    
    # Ссылки
    LOGIN_LINK_ON_REGISTER = (By.XPATH, "//a[contains(., 'Войти')]")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(., 'Восстановить пароль')]")
    REGISTER_LINK = (By.XPATH, "//a[contains(., 'Зарегистрироваться')]")
    
    # Меню продуктов
    SAUCES_TAB = (By.XPATH, "//span[contains(., 'Соусы')]/parent::div")
    FILLINGS_TAB = (By.XPATH, "//span[contains(., 'Начинки')]/parent::div")
    BUNS_TAB = (By.XPATH, "//span[contains(., 'Булки')]/parent::div")
    
    # Разделы продуктов (для проверки)
    SAUCES_SECTION = (By.XPATH, "//h2[contains(., 'Соусы')]")
    FILLINGS_SECTION = (By.XPATH, "//h2[contains(., 'Начинки')]")
    BUNS_SECTION = (By.XPATH, "//h2[contains(., 'Булки')]")
    
    # Ошибки
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]")
    PASSWORD_ERROR_MESSAGE = (By.XPATH, "//p[contains(., 'Некорректный пароль')]")

    # Проверки значений в input
    NAME_CHECK_INPUT = (By.XPATH, "//input[contains(., 'TestName')]")
    EMAIL_CHECK_INPUT = (By.XPATH, "//input[contains(., 'testtestov5299@yandex.ru')]")
    PASSWORD_CHECK_INPUT = (By.XPATH, "//input[contains(., 'Qwerty123')]")