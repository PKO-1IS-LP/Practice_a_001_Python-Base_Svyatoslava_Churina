def функця(x, y):
    # возвращает модуль суммы, сравнивает с единицей
    return abs(x + y) <= 1 and abs(-x + y) <= 1

x = float(input("Введите число x:"))  # вещественные данные (с запятой)
y = float(input("Введите число y:"))

if функця(x, y):
    print("YES")
else:
    print("NO")
