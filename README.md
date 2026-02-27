# Решение задач на попадание точки в область

Здесь представлены решения задач на проверку принадлежности точки с координатами `(x, y)` заданной области на плоскости.

## Задача 1: Квадрат

**Условие:** Принадлежит ли точка квадрату со стороной 2, центр которого совпадает с началом координат?

**График:**

<img width="386" height="592" alt="График квадрата" src="https://github.com/user-attachments/assets/5338227b-7696-4f3d-a68b-ed4bfd5ecf83" />

**Визуализация условия:**

<img width="327" height="318" alt="Область квадрата" src="https://github.com/user-attachments/assets/178a57f0-3668-49e5-9b24-0f5d309e01bf" />



**Код:**
```python
def функция(x, y):
    # Возвращает True, если оба условия выполняются ( abs(x)<=1 И abs(y)<=1 )
    return abs(x) <= 1 and abs(y) <= 1

x = float(input("Введите число x:"))  # Ввод вещественного числа
y = float(input("Введите число y:"))

if функция(x, y):
    print("YES")
else:
    print("NO")
```

**Вывод(попадает ли в область):**

<img width="675" height="90" alt="image" src="https://github.com/user-attachments/assets/0fee54fc-70eb-403c-ad8c-d2d525fe2e64" />


## Задача 2: Ромб

**Условие:** Принадлежит ли точка ромбу?

**График условия:**

<img width="329" height="843" alt="image" src="https://github.com/user-attachments/assets/37bc8aa2-4226-4cfa-a488-9ccb86e735c1" />

**Визуализация области:**

<img width="256" height="255" alt="image" src="https://github.com/user-attachments/assets/a57437d5-ad83-4a6b-995a-807682694d7b" />

**Код:**

```python
def функця(x, y):
    # возвращает модуль суммы, сравнивает с единицей
    return abs(x + y) <= 1 and abs(-x + y) <= 1

x = float(input("Введите число x:"))  # вещественные данные (с запятой)
y = float(input("Введите число y:"))

if функця(x, y):
    print("YES")
else:
    print("NO")
```

**Вывод(попадает ли в область):**

<img width="755" height="90" alt="image" src="https://github.com/user-attachments/assets/23ceeec3-2efb-49c9-a445-9a6a41fa6354" />


## Тренировочная задача: Круг

**Условие:** Принадлежит ли точка кругу радиусом 1 с центром в начале координат?

**Визуализация условия:**

<img width="480" height="479" alt="image" src="https://github.com/user-attachments/assets/48eaae25-baf6-46df-b221-7eebacc70989" />

**График условия:**

<img width="328" height="256" alt="image" src="https://github.com/user-attachments/assets/203006b1-afca-4696-9154-747d85a9c0b1" />

**Код:**

```python
def функция(x, y):
    # x**2 + y**2 всегда неотрицательно, поэтому abs() не нужен.
    # Возвращает True, если точка внутри круга или на его границе.
    return (x**2 + y**2) <= 1

x = float(input("Введите число x:"))
y = float(input("Введите число y:"))

if функция(x, y):
    print("YES")
else:
    print("NO")
```    

**Вывод(попадает ли в область):**

<img width="834" height="94" alt="image" src="https://github.com/user-attachments/assets/3f7d3958-fd2e-48a9-b4ed-f947cfedbdbd" />


## Задача 3 

**Условие:** Принадлежит ли точка закрашенной области, образованной кругом и двумя прямыми?

**График условия:**

<img width="326" height="697" alt="image" src="https://github.com/user-attachments/assets/30025039-3cc6-4569-9f47-c6917ecbcb73" />

**Визуализация условия:**

<img width="558" height="560" alt="image" src="https://github.com/user-attachments/assets/912cc32c-4335-42c8-8fd8-6fbc2880abe1" />

<img width="248" height="229" alt="image" src="https://github.com/user-attachments/assets/1592eb9c-d314-4da3-aad6-c3b4a858a192" />

**Код:**

```python
def функця(x,y):
    return ((x + 1)**2 + (y - 1)**2 <= 4 and -x - y <= 0 and -2*x + y >= 2) or (((x + 1)**2 + (y - 1)**2 >= 4) and -x - y >= 0 and -2*x + y <= 2) # возвращает модуль числа, то что в скобках, потом сравнивает это с единицей(<=1)
# or  и and нужно отделять друг от друга скобками, чтобы питон воспринимал их, как две отдельные задачи
x = float(input("Введите число:")) # вещественные данные(с запятой)
y = float(input("Введите число:"))

if функця(x,y):
    print("YES")
else:
    print("NO")


# (x + 1)**2 + (y - 1)**2 <= 4 то, что внутри окружности, (x + 1)**2 + (y - 1)**2 >= 4 за пределами окружности
# -x - y <= 0 and -2*x + y >= 2 две стороны полосочек, создающих карман и наоборот -x - y >= 0 and -2*x + y <= 2
```

**Вывод(попадает ли в область):**

<img width="746" height="99" alt="image" src="https://github.com/user-attachments/assets/de96942f-0d37-4a7b-b724-81bb69874c75" />





## Задача 4 (парабола)
**Условие:** найти точки вхождения в область гипербол (не учитывая границы)

**График условия:**

<img width="316" height="144" alt="image" src="https://github.com/user-attachments/assets/9214aba0-4bab-44b6-a309-9a72b7947513" />

**Визуализация условия:**

<img width="268" height="603" alt="image" src="https://github.com/user-attachments/assets/956f6729-1668-481e-b404-302fa889a920" />

**Код:**

```python
def функця(x,y):
    return (x**2 < y) or (-x**2 > y)# x должен быть меньше y, чтобы не выходить наружу, а оставаться внутри
# в обратном случае(отрицательная парабола), x расширяется, а y идет вниз(уменьшается), поэтому x больше y
# or и and нужно отделять друг от друга скобками, чтобы питон воспринимал их, как две отдельные задачи
x = float(input("Введите число:")) # вещественные данные(с запятой)
y = float(input("Введите число:"))

if функця(x,y):
    print("YES")
else:
    print("NO")
```

**Вывод(попадает ли в область):**

<img width="810" height="89" alt="image" src="https://github.com/user-attachments/assets/ae94913b-9ab8-4205-82a8-0d64a01023d1" />




```python
import os
import subprocess
import time


def clear():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


def show_main_menu():
    clear()
    print("\n--- Главное меню ---")
    print("1. Книги")
    print("2. Фильмы")
    print("3. Выход")


def Genre_book():
    clear()
    print("\n--- Жанр ---")
    print("1. Ужасы")
    print("2. Фэнтези")
    print("3. Назад")

def two():
    clear()
    print("\n--- Жанр ---")
    print("1. Исторические фильмы")
    print("2. Фэнтези")
    print("3. Назад")

def Author_Ywasi():
    clear()
    print("\n--- Авторы ---")
    print("1. Стивен Кинг")
    print("2. Франк Тилье")
    print("3. Назад")


def Book_Fentesi():
    clear()
    print("\n--- Книги ---")
    print("1. Хроники Нарнии")
    print("2. Властелин колец")
    print("3. Назад")


def Book_C_K():
    clear()
    print("\n--- Книги ---")
    print("1. Оно")
    print("2. Кладбище домашних животных")
    print("3. Назад")

def Book_F_T():
    clear()
    print("\n--- Книги ---")
    print("1. Переломы")
    print("2. Головоломка")
    print("3. Назад")

def content_Perelomi():
    clear()
    print("\n--- Содержание ---")
    print("""1. Девушка по имени Алиса страдает от «черных дыр» в памяти, и вскоре вокруг неё начинают
     происходить пугающие события: появляется фотография её давно погибшей сестры-близнеца, а на отца 
     совершено нападение . Расследование вскрывает жуткую связь между этими происшествиями, травмой, 
     пережитой её отцом во время войны в Ливане, и изощренным планом мести, корни которого уходят в 
     далекое прошлое""")
    print("2. Назад")

def content_Perelomi():
    clear()
    print("\n--- Содержание ---")
    print("""1. Девушка по имени Алиса страдает от «черных дыр» в памяти, и вскоре вокруг неё начинают
     происходить пугающие события: появляется фотография её давно погибшей сестры-близнеца, а на отца 
     совершено нападение . Расследование вскрывает жуткую связь между этими происшествиями, травмой, 
     пережитой её отцом во время войны в Ливане, и изощренным планом мести, корни которого уходят в 
     далекое прошлое""")
    print("2. Назад")

def content_Golovolomka():
    clear()
    print("\n--- Содержание ---")
    print("""1. Главный герой Илан вместе с бывшей девушкой ввязывается в таинственную игру «Паранойя», 
    которая проходит в стенах заброшенной психиатрической лечебницы, где восемь участников начинают 
    погибать один за другим . Пытаясь выжить и разгадать правила игры, Илан понимает, что всё происходящее 
    может иметь прямое отношение к загадочной смерти его родителей, и граница между реальностью и безумием 
    окончательно стирается """)
    print("2. Назад")

def content_Ono():
    clear()
    print("\n--- Содержание ---")
    print("""1. Семеро детей, объединившись в «Клуб неудачников», противостоят древнему злу, которое "
    "принимает обличие их самых сокровенных страхов, чаще всего являясь в виде клоуна Пеннивайза. "
    "Победив монстра в детстве, они дают клятву вернуться в родной город, если кошмар повторится. "
    "Спустя 27 лет чудовище пробуждается вновь, и повзрослевшие герои вынуждены сдержать обещание "
    "и вступить с «Оно» в последнюю схватку.""")
    print("2. Назад")

def content_Kladbishe():
    clear()
    print("\n--- Содержание ---")
    print("""1. Семья Кридов переезжает в дом рядом с оживленной трассой и мистическим индейским кладбищем, 
    способным возвращать мертвых к жизни. После гибели кота, а затем и маленького сына, глава семьи Луис, 
    поддавшись отчаянию, использует силу кладбища, чтобы воскресить их. Это решение оборачивается кошмаром, 
    ведь вернувшиеся с того света становятся воплощением зла.""")
    print("2. Назад")


def main():
    while True:
        show_main_menu()

        choice = input("Выберите действия 1-3: ").strip()

        if choice == "1":
            while True:
                Genre_book()
                choice = input("Выберите действия 1-3: ").strip()

                if choice == "1":
                    Author_Ywasi()
                    clear()
                    choice = input("Выберите действия 1-3: ").strip()

                    if choice == "1":
                        Book_C_K()
                        clear()
                        choice = input("Выберите действия 1-3: ").strip()

                        if choice == "1":
                            content_Ono()
                            clear()
                            choice = input("Выберите действия 1-3: ").strip()

                        elif choice == "2":
                            content_Kladbishe()
                            choice = input("Выберите действия 1-3: ").strip()
                            clear()

                        elif choice == "3":
                            break
                        else:
                            clear()
                            print("Неверный выбор")
                            time.sleep(1.4)

                    if choice == "2":
                        Book_F_T()
                        clear()
                        choice = input("Выберите действия 1-3: ").strip()

                        if choice == "1":
                            content_Perelomi()
                            clear()
                            choice = input("Выберите действия 1-3: ").strip()

                        elif choice == "2":
                            content_Golovolomka()
                            clear()
                            choice = input("Выберите действия 1-3: ").strip()

                        elif choice == "3":
                            break
                        else:
                            clear()
                            print("Неверный выбор")
                            time.sleep(1.4)

                if choice == "2":
                    Book_Fentesi()
                    clear()
                    choice = input("Выберите действия 1-3: ").strip()

                    if choice == "1":
                        content_Ono()
                        clear()
                        choice = input("Выберите действия 1-3: ").strip()















                elif choice == "3":
                    break
                else:
                    clear()
                    print("Неверный выбор")
                    time.sleep(1.4)

        elif choice == "2":
            while True:
                two()
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


```

