import os
import subprocess
import time


def clear():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


def show_main_menu():
    clear()
    print("--- Главное меню ---")
    print("1. Задача 1: Квадрат")
    print("2. Задача 2: Ромб")
    print("3. Задача 3: Сложная")
    print("4. Выход")


def Zadacha_1(x, y):
    clear()
    print("--- Задача 1 ---")
    print("Условие: Принадлежит ли точка квадрату со стороной 2, центр которого совпадает с началом координат?")
    return abs(x) <= 1 and abs(y) <= 1


def Zadacha_2(x, y):
    clear()
    print("--- Задача 2 ---")
    print("Условие: Принадлежит ли точка ромбу?")
    return abs(x + y) <= 1 and abs(-x + y) <= 1


def Zadacha_3(x, y):
    clear()
    print("--- Задача 3 ---")
    print("Условие: Принадлежит ли точка закрашенной области, образованной кругом и двумя прямыми?")
    return ((x + 1) ** 2 + (y - 1) ** 2 <= 4 and -x - y <= 0 and -2 * x + y >= 2) or (
            ((x + 1) ** 2 + (y - 1) ** 2 >= 4) and -x - y >= 0 and -2 * x + y <= 2)


def main():
    while True:
        show_main_menu()
        choice = input("Выберите пункт меню (1-4): ").strip()

        if choice in ("1", "2", "3"):
            clear()
            x = float(input("Введите координату x: "))
            y = float(input("Введите координату y: "))

            if choice == "1":
                result = Zadacha_1(x, y)
            elif choice == "2":
                result = Zadacha_2(x, y)
            else:
                result = Zadacha_3(x, y)

            if result:
                print("YES (точка принадлежит области)")
            else:
                print("NO (точка не принадлежит области)")

            input("Нажмите Enter, чтобы вернуться в главное меню...")

        elif choice == "4":
            clear()
            print("До свидания!")
            break
        else:
            clear()
            print("Неверный ввод. Попробуйте снова.")
            time.sleep(1.5)


if __name__ == "__main__":
    main()