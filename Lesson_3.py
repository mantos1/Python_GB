# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
def Exp1():
    list = []
    list = input('Укажите числа через запятую: \n').split(',')
    result = 0
    i = 0
    while i < len(list):
        if float(i) % 2 != 0:
            result += int(list[i])
        i += 1
    print(result)


# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import math
def Exp2():
    list = []
    list = input('Укажите числа через запятую: \n').split(',')
    i = 0
    list_result = []
    while i < math.ceil(len(list) / 2):
        list_result.append(int(list[i]) * int(list[-i-1]))
        i += 1
    print(list_result)

# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def Exp3():
    list = []
    list = map(lambda x: round(x%1, 2), map(float, input('Укажите вещественные числа через запятую: \n').split(',')))
    ii = 0
    max = 0
    min = 0
    for i in list:
        if ii == 0:
            min = i
            max = i
        if i != 0:
            if i > max:
                max = i
            elif i < min:
                min = i
        ii += 1
    print(max - min)


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
def Exp4():
    num = int(input('Введите число :\n'))
    bin = ''
    while num > 0:
        bin = str(num % 2) + bin
        num = num // 2
    print(bin)

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи](https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:~:text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0%B8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8.)
def Exp5():
    num = int(input('Введите число: \n'))
    list_fib = [0,1]
    list_negfib = [0,1]
    for i in range(2,num+1):
        list_fib.append(list_fib[i-1] + list_fib[i-2])
        list_negfib.append(list_negfib[i-2] - list_negfib[i-1])
    list_negfib.reverse()
    print(list_negfib[:num-1] + list_fib)
