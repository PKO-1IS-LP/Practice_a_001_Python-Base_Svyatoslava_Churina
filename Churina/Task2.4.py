i = map(int,input("Введите числа: ").split())
b = 0
for a in i:
    if a % 2 == 0:
       if b < a:
            b = a
    if a % 2 == 1:
        print("Нечетное")
print("Максимальное четное число: ",b)