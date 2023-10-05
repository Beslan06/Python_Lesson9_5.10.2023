# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.


import random  # Импортируем модуль random для генерации случайных чисел.

# Создаем декоратор validate_input, который будет проверять входные данные и при необходимости генерировать случайные числа.
def validate_input(guess_func):
    # Создаем обертку (wrapper) для декоратора.
    def wrapper(min_number, max_number, max_attempts):
        # Проверяем, входят ли переданные значения в допустимые диапазоны [1, 100] и [1, 10].
        if min_number < 1 or max_number > 100 or max_attempts < 1 or max_attempts > 10:
            # Если значения не входят в диапазоны, генерируем случайные значения.
            min_number = random.randint(1, 100)
            max_number = random.randint(1, 100)
            max_attempts = random.randint(1, 10)
            print("Переданные числа не входят в диапазоны [1, 100] и [1, 10]. Генерируются случайные значения.")

        # Вызываем функцию guess_func с корректными значениями.
        return guess_func(min_number, max_number, max_attempts)
    
    return wrapper

# Определяем функцию guess, которая будет угадывать число.
@validate_input  # Применяем декоратор validate_input к функции guess.
def guess(min_number, max_number, max_attempts):
    # Генерируем случайное загаданное число в заданном диапазоне.
    secret_number = random.randint(min_number, max_number)
    attempts_left = max_attempts

    while attempts_left > 0:
        # Запрашиваем у пользователя ввод числа.
        user_guess = input(f"Угадайте число от {min_number} до {max_number}. У вас {attempts_left} попыток: ")
        try:
            user_guess = int(user_guess)  # Преобразуем введенный текст в целое число.
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

# Пример использования декорированной функции:
guess(1, 100, 5)  # Вызываем функцию с переданными значениями.
