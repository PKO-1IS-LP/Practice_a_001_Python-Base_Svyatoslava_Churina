 1. int()
Преобразует строку в целое число.
s = "25"
number = int(s)
print(number)

2. range()
Создаёт последовательность чисел для цикла(исключая последнее число).
for i in range(1,10,2): # от 1 до 10, берет каждое второе число
    print(i)
----------------------------------------------
for i in range(55,99,3):
    print(i)

3. len()
Возвращает длину строки или списка.

Пример со строкой
s = "hello world"
print(len(s))
---------------
Пример со списком
numbers = [10, 20, 30, 40, 50, 60, 70]
print(len(numbers))


4. list()
Создаёт список или преобразует объект в список.
numbers = list(map(int, ["3", "6", "5"]))
print(numbers)
--------------
x = list("hello")
print(x)
-------------
a = list("hello")
b = list("world")
print(a+b)


5.Типы данных
1) Целочисленные int() 5
2) Строковые str() "5"
3) Логические bool()
4) Вещественные (пример: 3,1234 ) flout()

a = int(5)
b = int(5)
print(a+b)
a = str(5)
b = str(5)
print(a+b)
print(type(a))
print(type(b))

-------------

a = "5"
b = 5
print(type(a))
print(type(b))

s = int(40)
c = int(10)
a = int(5)
b = int(5)
print(a+b+c+s)

print(type(a))
print(type(b))
print(type(c))
print(type(s))

s = str(30)
c = str(10)
a = str(5)
b = str(5)
print(a+b+c+s)

print(type(a))
print(type(b))
print(type(c))
print(type(s))

--------------

a = "5"
b = 5
print(type(a))
print(type(b))

s_new = int(40)
c_new = int(10)
a_new = int(5)
b_new = int(5)

print(type(a_new))
print(type(b_new))
print(type(c_new))
print(type(s_new))

s = str(30)
c = str(10)
a = str(5)
b = str(5)
print(a+b+c+s,a_new+b_new+s_new+c_new)

print(type(a))
print(type(b))
print(type(c))
print(type(s))

------------------------------------
6. .isdigit()
Проверяет, является ли символ цифрой.

s = "5"
a = "5,1"
b = "а"
# Проверяем, является ли строка цифрой
print(s.isdigit())
print(a.isdigit())
print(b.isdigit())
print(type(s))

7. .isalpha()
Проверяет, является ли символ буквой

a = "Д"
b = "7"
print(a.isalpha())  # True
print(b.isalpha())  # False

8. .isupper()
Проверяет, заглавная ли буква.

a = input()
#если в "а" есть заглавные буквы, то выведи True
if (a.isupper()):
    print(True)
else:# иначе
    print(False)
print(f"""Введенное значение:{a}""")

9.map()
Применяет функцию к каждому элементу.

float_numbers = [1.5, 2.7, 3.9, 4.2, 5.0] # изначальные цифра
numbers = list(map(int, [1.5, 2.7, 3.9, 4.2, 5.0])) # создание списка из них, применение функции к каждому элементу, видоизменение чисел
print(float_numbers, numbers) # вывод изначальных цифр и конечного результата
print(type(numbers)) # тип данных

10.  append()
Добавляет элемент в конец списка.

Список = ["банан", "молоко", "яблоко", "макароны", "сыр"]
Список.append("сливки")
print(Список)

11. break
Останавливает цикл.

for a in range(1,7):
    if a % 7 == 0:
       break
print(a)

12. Логические операторы

and

Оба условия должны быть истинны.

if x > 0 and x < 10:

or

Хотя бы одно условие истинно.

if x < 0 or x > 100:


13. Оператор % (остаток)
Возвращает остаток от деления.

for a in range(1589764291,7357840347846):
    if a % 7 == 0:
        print(a)
    else:
        print(0)

14.  Индексация [i]
Позволяет обратиться к элементу по номеру.

s = "hello"
print(s[0])  # h
print(s[4])  # o

------------------------

s = "HTTP encoding library list operations Parse yaml text hierarchy object null"
print(s[0],s[5],s[14],s[22],s[8],s[4],s[3],s[20],s[25],s[54],s[27],s[6])

---------------------------------------------------------------------------

s = "HTTP encoding library list operations Parse yaml text hierarchy object null"
print(s[0])
print(s[5])
print(s[14])
print(s[22])
print(s[8])
print(s[4])
print(s[3])
print(s[20])
print(s[25])
print(s[54])
print(s[27])
print(s[6])

----------------------------------------------------------------------------

s = "level"

print(s[0])  # l
print(s[4])  # l
print(s[0] == s[4])  # True

print(s[1])  # e
print(s[3])  # e
print(s[1] == s[3])  # True
