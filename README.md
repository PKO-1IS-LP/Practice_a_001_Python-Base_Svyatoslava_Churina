<img width="386" height="592" alt="image" src="https://github.com/user-attachments/assets/5338227b-7696-4f3d-a68b-ed4bfd5ecf83" />

<img width="327" height="318" alt="image" src="https://github.com/user-attachments/assets/178a57f0-3668-49e5-9b24-0f5d309e01bf" />

def функця(x,y):
    return abs(x) <=1 and abs(y) <=1 # возвращает модуль числа, то что в скобках, потом сравнивает это с единицей(<=1) 

x = float(input("Введите число:")) # вещественные данные(с запятой)
y = float(input("Введите число:"))

if функця(x,y): 
    print("YES")
else:
    print("NO")



Задача 2 графики


def функця(x,y):
    return abs(x+y) <=1 and abs(-x+y) <=1 # возвращает модуль числа, то что в скобках, потом сравнивает это с единицей(<=1)

x = float(input("Введите число:")) # вещественные данные(с запятой)
y = float(input("Введите число:"))

if функця(x,y):
    print("YES")
else:
    print("NO")

    

<img width="329" height="843" alt="image" src="https://github.com/user-attachments/assets/37bc8aa2-4226-4cfa-a488-9ccb86e735c1" />

<img width="256" height="255" alt="image" src="https://github.com/user-attachments/assets/a57437d5-ad83-4a6b-995a-807682694d7b" />



Задача, тренировка, круг


def функця(x,y):
    return abs(x**2+y**2) <= 1 # возвращает модуль числа, то что в скобках, потом сравнивает это с единицей(<=1)

x = float(input("Введите число:")) # вещественные данные(с запятой)
y = float(input("Введите число:"))

if функця(x,y):
    print("YES")
else:
    print("NO")
    

<img width="480" height="479" alt="image" src="https://github.com/user-attachments/assets/48eaae25-baf6-46df-b221-7eebacc70989" />


<img width="328" height="256" alt="image" src="https://github.com/user-attachments/assets/203006b1-afca-4696-9154-747d85a9c0b1" />


Задача 3

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



<img width="558" height="560" alt="image" src="https://github.com/user-attachments/assets/912cc32c-4335-42c8-8fd8-6fbc2880abe1" />

<img width="326" height="697" alt="image" src="https://github.com/user-attachments/assets/30025039-3cc6-4569-9f47-c6917ecbcb73" />

