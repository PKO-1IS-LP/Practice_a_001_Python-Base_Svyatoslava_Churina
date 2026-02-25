a = input("Введите строку: ")
b = input("Введите символ: ")
c = -1
for c in a: # перебирает символы из строки(а)
    if c == a:
        break
    print(c)
else:
    print("Не найден")

