import math
import csv
import json
import os
import functools
import random

# Декоратор для сохранения параметров и результатов в JSON файл
def save_to_json(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        data = {
            "args": args,
            "kwargs": kwargs,
            "result": result
        }
        filename = f"{func.__name__}.json"

        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                json.dump([data], file, indent=4)
        else:
            with open(filename, 'r') as file:
                existing_data = json.load(file)
            existing_data.append(data)
            with open(filename, 'w') as file:
                json.dump(existing_data, file, indent=4)

        return result
    return wrapper

# Функция нахождения корней квадратного уравнения
def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return "No real roots"

# Функция генерации CSV файла
def generate_csv_file(filename, num_rows):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(num_rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            writer.writerow(row)
