# Задание №6
# Доработайте прошлую задачу добавив декоратор wraps в
# каждый из декораторов.

import json  # Импортируем модуль json для работы с JSON файлами.
import os    # Импортируем модуль os для работы с файловой системой.
import functools  # Импортируем модуль functools для обертки функции и сохранения её имени.
import random  # Импортируем модуль random для генерации случайных чисел.

# Декоратор для сохранения параметров и результатов в JSON файл.
def save_to_json(func):
    @functools.wraps(func)  # Сохраняем имя и атрибуты декорируемой функции.
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # Вызываем декорируемую функцию и сохраняем её результат.
        filename = f"{func.__name__}.json"  # Генерируем имя файла на основе имени декорируемой функции.

        if not os.path.exists(filename):  # Проверяем, существует ли файл.
            data = []  # Если файл не существует, создаем пустой список данных.
        else:
            with open(filename, 'r') as file:
                data = json.load(file)  # Если файл существует, загружаем данные из него.

        entry = {
            "args": args,    # Сохраняем позиционные аргументы функции.
            "kwargs": kwargs,  # Сохраняем ключевые аргументы функции.
            "result": result  # Сохраняем результат выполнения функции.
        }

        data.append(entry)  # Добавляем запись с параметрами и результатом в список данных.

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)  # Записываем данные в файл с отступами для удобства чтения.

        return result  # Возвращаем результат выполнения декорируемой функции.

    return wrapper  # Возвращаем обертку (wrapper) декоратора.

# Декоратор для проверки диапазона значений входных параметров.
def validate_input(func):
    @functools.wraps(func)  # Сохраняем имя и атрибуты декорируемой функции.
    def wrapper(min_number, max_number, max_attempts):
        if 1 <= min_number <= 100 and 1 <= max_attempts <= 10:
            return func(min_number, max_number, max_attempts)  # Вызываем декорируемую функцию с корректными значениями.
        else:
            min_number = random.randint(1, 100)  # Генерируем случайные значения, если значения не корректны.
            max_number = random.randint(1, 100)
            max_attempts = random.randint(1, 10)
            print("Переданные числа не входят в диапазоны [1, 100] и [1, 10]. Генерируются случайные значения.")
            return func(min_number, max_number, max_attempts)  # Вызываем декорируемую функцию с сгенерированными значениями.

    return wrapper  # Возвращаем обертку (wrapper) декоратора.

# Декоратор для многократного запуска функции.
def run_multiple_times(times):
    def decorator(func):
        @functools.wraps(func)  # Сохраняем имя и атрибуты декорируемой функции.
        def wrapper(*args, **kwargs):
            results = []  # Создаем список для хранения результатов выполнения функции.

            for _ in range(times):
                result = func(*args, **kwargs)  # Вызываем декорируемую функцию и сохраняем результат.
                results.append(result)  # Добавляем результат выполнения в список.

            return results  # Возвращаем список результатов.

        return wrapper  # Возвращаем обертку (wrapper) декоратора.

    return decorator  # Возвращаем декоратор decorator с параметром times.

# Пример использования всех декораторов для декорации функции угадайки.
@run_multiple_times(3)  # Применяем декоратор для многократного запуска (3 раза).
@validate_input  # Применяем декоратор для проверки диапазона значений.
@save_to_json  # Применяем декоратор для сохранения параметров и результатов.
def guess(min_number, max_number, max_attempts):
    secret_number = random.randint(min_number, max_number)
    attempts_left = max_attempts

    while attempts_left > 0:
        user_guess = input(f"Угадайте число от {min_number} до {max_number}. У вас {attempts_left} попыток: ")
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Введите целое число.")
            continue

        if user_guess == secret_number:
            print("Поздравляю! Вы угадали число!")
            break
        elif user_guess < secret_number:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")

        attempts_left -= 1

    if attempts_left == 0:
        print(f"Вы использовали все попытки. Загаданное число было {secret_number}.")

guess(1, 100, 5)
