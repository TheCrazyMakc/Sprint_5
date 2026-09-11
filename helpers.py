import random
import string


def generate_unique_email():
    """Генерирует уникальный email с случайным числом"""
    random_number = random.randint(100, 999)
    return f"testtestov52{random_number}@yandex.ru"


def generate_password(length=6):
    """Генерирует пароль заданной длины (по умолчанию 6 символов)"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))