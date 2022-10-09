# Задача 1
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
def Exp1():
    week_day = input('Введите номер дня недели:\n')
    if week_day.isdigit():
        week_day = int(week_day)
        if week_day >= 1 and week_day <= 7:
            if week_day >= 6:
                print('Да')
            else:
                print('Нет')
        else:
            print('Указан неверный номер дня недели')
    else:
        print('Необходимо ввести цифру номера недели')

# Задача 2
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def Exp2():
    list = range(2)
    for x in list:
        for y in list:
            for z in list:
                print(f'x = {x}, y = {y}, z = {z}', ' >>> ', f'not ({x} or {y} or {z}) == (not {x} and not {y} and not {z})')
                print(not (x or y or z), ' == ', (not x and not y and not z), ' >>> ', not (x or y or z) == (not x and not y and not z), '\n')

# Задача 3
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
def Exp3():
    try:
        x = int(input('Введите значение Х: \n'))
        y = int(input('Введите значение Y: \n'))
        if x != 0 and y != 0:
            if x > 0 and y > 0:
                return_value = '1 четверть'
            elif x < 0 and y > 0:
                return_value = '2 четверть'
            elif x < 0 and y < 0:
                return_value = '3 четверть'
            elif x > 0 and y < 0:
                return_value = '4 четверть'
            print(return_value)
        else:
            print('Значения кооринаты точки не могут иметь 0')
    except:
        print('Необходимо вводить цифры')

# Задача 4
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
def Exp4():
    try:
        number = int(input('Введите номер четверти: \n'))
        if number >= 1 and number <= 4:
            if number == 1:
                return_value = 'x > 0, y > 0'
            elif number == 2:
                return_value = 'x < 0, y > 0'
            elif number == 3:
                return_value = 'x < 0, y < 0'
            elif number == 4:
                return_value = 'x > 0, y < 0'
            print(return_value)
        else:
            print('Указан некорректный номер')
    except:
        print('Необходимо вводить цифры')

# Задача 5
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

def Exp5():
    try:
        a1 = float(input('Введите значение A1: \n'))
        a2 = float(input('Введите значение A2: \n'))
        b1 = float(input('Введите значение B1: \n'))
        b2 = float(input('Введите значение B2: \n'))

        print(round(math.sqrt(math.pow((a1 - b1), 2) + math.pow((a2 - b2), 2)), 2))
    except:
        print('Необходимо вводить цифры')
