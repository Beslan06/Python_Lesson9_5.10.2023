# Задание №4
# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

import functools  # Импортируем модуль functools для обертки функции и сохранения её имени.

# Создаем декоратор run_multiple_times с параметром times (количество запусков).
def run_multiple_times(times):
    # Создаем декоратор decorator, который принимает декорируемую функцию func.
    def decorator(func):
        # Обертка wrapper для декорируемой функции.
        @functools.wraps(func)  # Сохраняем имя и атрибуты декорируемой функции.
        def wrapper(*args, **kwargs):
            results = []  # Создаем список для хранения результатов выполнения функции.

            # Запускаем декорируемую функцию times раз и сохраняем результаты в списке.
            for _ in range(times):
                result = func(*args, **kwargs)
                results.append(result)  # Добавляем результат выполнения в список.

            return results  # Возвращаем список результатов.

        return wrapper  # Возвращаем обертку (wrapper) декоратора.

    return decorator  # Возвращаем декоратор decorator с параметром times.

# Пример использования декоратора с параметром.
@run_multiple_times(3)  # Указываем количество запусков функции (3 раза).
def example_function(x, y=0):
    return x + y

# Пример вызова декорированной функции.
results = example_function(3, y=2)
print(f"Результаты: {results}")
