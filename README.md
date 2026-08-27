Ресурс, который проверяем:

https://stellarburgers.education-services.ru/


Чтобы выполнить все проверки сразу, нужно запустить файл: run_all_tests.py


Список проверок:

test_1_registration.py - успешная регистрация

test_2_registration_again.py - повторная регистрация с таким же email

test_3_registration_failed_empty_name.py - регистрация с пустым именем ("")

test_4_registration_failed_mail.py - проверка ввода неверного email (testtestov5299#yandex.ru)

test_5_registration_failed_pass.py - проверка пароля короче 6 символов (12345)

test_6_login_main.py - вход по кнопке «Войти в аккаунт» на главной

test_7_login_lk.py - вход через кнопку «Личный кабинет»

test_8_login_from_reg.py - вход через кнопку в форме регистрации

test_9_login_from_forget_pass.py - вход через кнопку в форме восстановления пароля

test_10_main_to_lk.py - переход по клику на «Личный кабинет»

test_10_main_to_lk.py - переход по клику на «Личный кабинет» авторизированного пользователя

test_11_lk_to_constr.py - переход по клику на «Конструктор»

test_12_lk_to_main.py - переход по клику на логотип Stellar Burgers

test_13_exit.py - выход по кнопке «Выйти» в личном кабинете

test_14_food_menu.py - переходы к разделам: «Булки», «Соусы», «Начинки».


ЛОКАТОРЫ

кнопка "Войти в аккаунт"
(By.XPATH, "//button[contains(., 'Войти в аккаунт')]")

кнопка "Зарегистрироваться"
(By.XPATH, "//a[contains(., 'Зарегистрироваться')]")

поле Имя при регистрации
(By.XPATH, "//label[text()='Имя']/following-sibling::input")

поле Email при регистрации или входе
(By.XPATH, "//label[text()='Email']/following-sibling::input")

поле Пароль при регистрации или входе
(By.XPATH, "//label[text()='Пароль']/following-sibling::input")

кнопка Зарегистрироваться
(By.XPATH, "//button[contains(., 'Зарегистрироваться')]")

кнопка Войти
(By.CSS_SELECTOR, ".button_button__33qZ0")

кнопка "Личный кабинет"
(By.XPATH, "//p[contains(., 'Личный Кабинет')]")

кнопка "Войти" на странице регистрации
(By.XPATH, "//a[contains(., 'Войти')]")

кнопка "Восстановить пароль"
(By.XPATH, "//a[contains(., 'Восстановить пароль')]")

кнопка "Войти" на странице Восстановить пароль
(By.XPATH, "//a[contains(., 'Войти')]")

кнопка "Конструктор"
(By.XPATH, "//p[contains(., 'Конструктор')]")

кнопка с логотипом и переходом на главную страницу
(By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2")

кнопка выхода из личного кабинета
(By.XPATH, "//button[contains(., 'Выход')]")

