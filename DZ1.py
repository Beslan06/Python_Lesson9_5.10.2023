# Решить задачи, которые не успели решить на семинаре.
# Напишите следующие функции:
    #  Нахождение корней квадратного уравнения
    #  Генерация csv файла с тремя случайными числами в каждой строке.
    # 100-1000 строк.
    #  Декоратор, запускающий функцию нахождения корней квадратного
    # уравнения с каждой тройкой чисел из csv файла.
    #  Декоратор, сохраняющий переданные параметры и результаты работы
    # функции в json файл.
# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

import math  # Импортируем модуль math для выполнения математических операций.
import csv   # Импортируем модуль csv для работы с CSV файлами.
import random  # Импортируем модуль random для генерации случайных чисел.
import json  # Импортируем модуль json для работы с JSON файлами.
import os    # Импортируем модуль os для работы с файловой системой.
import functools  # Импортируем модуль functools для работы с функциями и декораторами.

# Функция нахождения корней квадратного уравнения
def quadratic_roots(a, b, c):
    # Вычисляем дискриминант.
    discriminant = b**2 - 4*a*c
    
    # Проверяем, есть ли действительные корни.
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return "Нет действительных корней"

# Функция генерации CSV файла с числами
def generate_csv(filename, num_rows):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(num_rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            writer.writerow(row)

# Декоратор для выполнения функции с данными из CSV файла
def quadratic_roots_decorator(func):
    def wrapper_from_csv(csv_filename):
        with open(csv_filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                roots = func(a, b, c)
                print(f"Для коэффициентов {a}, {b}, {c} корни: {roots}")
    return wrapper_from_csv

# Декоратор для сохранения параметров и результатов в JSON файл
def save_to_json(func):
    @functools.wraps(func)  # Используем декоратор functools.wraps для сохранения имени и атрибутов функции.
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # Вызываем декорируемую функцию и сохраняем результат.
        data = {
            "args": args,   # Сохраняем позиционные аргументы функции.
            "kwargs": kwargs,  # Сохраняем ключевые аргументы функции.
            "result": result  # Сохраняем результат выполнения функции.
        }
        filename = f"{func.__name__}.json"  # Генерируем имя JSON файла на основе имени функции.

        if not os.path.exists(filename):  # Проверяем, существует ли файл.
            with open(filename, 'w') as file:
                json.dump([data], file, indent=4)  # Если файл не существует, создаем новый и записываем данные.
        else:
            with open(filename, 'r') as file:
                existing_data = json.load(file)  # Если файл существует, загружаем существующие данные.
            existing_data.append(data)  # Добавляем новые данные к существующим.
            with open(filename, 'w') as file:
                json.dump(existing_data, file, indent=4)  # Записываем обновленные данные обратно в файл.

        return result  # Возвращаем результат выполнения функции.
    return wrapper  # Возвращаем обертку (wrapper) декоратора.

# Пример использования:
if __name__ == "__main__":
    generate_csv('random_numbers.csv', 100)  # Генерация CSV файла с 100 строками случайных чисел.
    quadratic_roots_decorator(quadratic_roots)('random_numbers.csv')  # Запуск функции с данными из CSV файла.
    save_to_json(quadratic_roots)(1, 2, 1)  # Сохранение параметров и результатов в JSON файл.
