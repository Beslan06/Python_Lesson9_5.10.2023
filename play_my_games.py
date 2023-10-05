import os

def main():
    games_directory = "games_package"

    while True:
        available_games = []

        # Получаем список файлов игр в папке games_package
        for foldername, subfolders, filenames in os.walk(games_directory):
            for filename in filenames:
                if filename.startswith("les") and filename.endswith(".py"):
                    game_name = os.path.splitext(filename)[0]
                    available_games.append(f"Игра {int(game_name[3:])}")

        print("Доступные игры:")
        for i, game_name in enumerate(available_games, start=1):
            print(f"{i}. {game_name}")

        choice = input("Введите номер игры (или 'q' для выхода): ")

        if choice.lower() == 'q':
            break  # Выход из цикла при вводе 'q'

        try:
            selected_game_index = int(choice) - 1
            if 0 <= selected_game_index < len(available_games):
                selected_game_name = available_games[selected_game_index]
                module_name = f"games_package.game{selected_game_index + 1}.les{selected_game_index + 1}"
                try:
                    game_module = __import__(module_name, fromlist=["play_game"])
                    game_function = getattr(game_module, "play_game", None)
                    if game_function:
                        result = game_function()
                        print(f"Результат: {result}")
                except ImportError:
                    print(f"Ошибка: не удалось импортировать игру {module_name}.")
            else:
                print("Неверный выбор игры. Пожалуйста, выберите номер из списка.")
        except ValueError:
            print("Неверный выбор игры. Пожалуйста, выберите номер из списка.")

if __name__ == "__main__":
    main()
