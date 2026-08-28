Ресурс, который проверяем:

https://stellarburgers.education-services.ru/


Чтобы выполнить все проверки сразу, нужно запустить файл: run_all_tests.py


Список проверок:

# Только тесты регистрации
pytest tests/ -v -s -m registration

# Только тесты входа
pytest tests/ -v -s -m login

# Только тесты навигации
pytest tests/ -v -s -m navigation

# Только тесты меню
pytest tests/ -v -s -m menu