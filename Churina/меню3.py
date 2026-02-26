import os
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_main_menu():
    clear()
    print("\n--- Главное меню ---")
    print("1. Начать работу")
    print("2. Настройки")
    print("3. Выход")


def submenu_one():
    clear()
    print("\n--- Меню 1 ---")
    print("1. Действие А")
    print("2. Действие Б")
    print("3. Назад")


def main():
    while True:
        show_main_menu()

        choice = input("Выберите дейсвтвия 1-3: ").strip()

        if choice == "1":
            while True:
                submenu_one()
                sub = input("→ ").strip()

                if sub in ("1", "2"):
                    clear()
                    print(f"Выполняется действие {sub}...")
                    time.sleep(2)
                elif sub == "3":
                    break
                else:
                    clear()
                    print("Неверный выбор")
                    time.sleep(1.4)

        elif choice == "2":
            clear()
            print("Настройки (пока пусто)")
            time.sleep(2)

        elif choice == "3":
            clear()
            print("До свидания...")
            time.sleep(1.2)
            clear()
            break

        else:
            clear()
            print("Неверный выбор")
            time.sleep(1.4)


main()