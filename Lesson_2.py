# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
def Exp1():
    number = input('Введите число:\n')
    result = 0
    for i in number:
        if i.isdigit():
            result += int(i)
    print(result)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def Exp2():
    number = int(input('Введите число N:\n'))
    list = []
    for i in range(1, number + 1):
        cnt = 1
        for x in range(1, i + 1):
            cnt *= x
        list.append(cnt)
    print(list)

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
def Exp3():
    number = int(input('Введите число N:\n'))
    list = []
    result = 0
    x = 0
    for i in range(1, number + 1):
        x = round((1+1/i)**i,2)
        list.append(f'{i}:' + str(x))
        result += x
    print(list)
    print(f'Сумма = {result} ' )


# *4. НЕОБЯЗАТЕЛЬНАЯ ЗАДАЧА
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.

import random
def Exp4():
    number = int(input('Введите число > 4:\n'))
    list = []
    i = 0
    while i < number:
        list.append(random.randrange(number*-1, number))
        i += 1
    result = 1
    with open('Lesson_2.txt', 'r', encoding='utf-8') as file:
        for line in file:
            result *= list[int(line.strip())]
    print(f'Список: {list} \nПроизведение: {result}')
    random.shuffle(list)
    print('Перемешанный список: ', list)

# ДОП. задача на алгоритмы с реальных собеседований
# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# (порядок не важен)
def Exp_Other():
    list1 = [1, 2, 3, 2, 0]
    list2 = [5, 1, 2, 7, 3, 2]
    print([value for value in list1 if value in list2])

