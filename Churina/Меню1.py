import os #- модуль работы с ОС
import time # - модуль работы с временем


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
        print("Тоже хорошо")

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
            time.sleep(1)
            print(">> прошла секунда")
            one()
        if choice == '2':
            print(">> Выполнение пункта 2...")
            time.sleep(1)
            print(">> прошла секунда")
            two()
        elif choice == '3':
            print(">> Выход из программы. До свидания!")
            break  # Выход из цикла while
        else:
            print(">> Неверный ввод, попробуйте снова.")
main()

