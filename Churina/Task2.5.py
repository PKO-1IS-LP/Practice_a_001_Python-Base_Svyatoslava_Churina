i = map(int,input("Введите числа: ").split())
b = 0
for a in i:
    if a % 2 == 1 and a > 10:
        b = b + a
print("Cумма: ",b)