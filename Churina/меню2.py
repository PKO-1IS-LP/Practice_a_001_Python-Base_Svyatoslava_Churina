import os
import time


def show_menu_for_one():
    print("\n--- Главное меню ---")
    print("1. Пункт 1: Начать работу")
    print("2. Пункт 2: Настройки")
    print("3. Выход")


def one():
    print("Меню 1")
    os.system('cls||clear')

def two():
    print("Меню 2")
    выбор = input("Выберите напиток(чай,сок,молоко): ")
    if выбор == "чай":
        print("Шикарный выбор")
    if выбор == "сок":
        print("Неплохо")
    if выбор == "молоко":
        print("Молоко с чаем прекрасно")

    os.system('cls||clear')

def show_menu():
    print("\n--- Главное меню ---")
    print("1. Пункт 1: Начать работу")
    print("2. Пункт 2: Настройки")
    print("3. Выход")


def main():
    while True:
        show_menu()
        choice = input("Выберите пункт (1-3): ")

        if choice == '1':
            print(">> Выполнение пункта 1...")
            time.sleep(5)
            print(">> прошла секунда")
            one()

            # Добавьте логику для пункта 1
        elif choice == '2':
            print(">> Открытие настроек...")
            time.sleep(3)
            os.system('cls||clear')
            two()
            # Добавьте логику для пункта 2
        elif choice == '3':
            print(">> Выход из программы. До свидания!")
            time.sleep(3)
            os.system('cls||clear')
            break  # Выход из цикла while
        else:
            print(">> Неверный ввод, попробуйте снова.")
            time.sleep(3)
            os.system('cls||clear')


main()