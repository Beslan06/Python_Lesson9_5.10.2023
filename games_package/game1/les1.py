# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# от 1 до 100 для загадывания,
# от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток. 

import random

def create_guess_game():
    secret_number = random.randint(1, 100)
    max_attempts = random.randint(1, 10)
    attempts_left = max_attempts

    def guess():
        nonlocal attempts_left

        while attempts_left > 0:
            user_guess = input(f"Угадайте число от 1 до 100. У вас {attempts_left} попыток: ")
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

    return guess

# Пример использования:
game = create_guess_game()
game()
