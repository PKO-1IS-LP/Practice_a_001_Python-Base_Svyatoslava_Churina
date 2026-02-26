def функця(x, y):
    # возвращает модуль числа, сравнивает его с единицей (<=1)
    return abs(x) <= 1 and abs(y) <= 1

x = float(input("Введите число x:"))  # вещественные данные (с запятой)
y = float(input("Введите число y:"))

if функця(x, y):
    print("YES")
else:
    print("NO")