i = int(input())
b = 0
c = 0
for a in range(1,i + 1):
    if a % 2 == 0:
        b = b + 1
    else:
        c = c + 1
print("Четные: ", b,"Нечетные: ",c)
