
import  random

# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
def Exp1():
    import random
    number = random.randint(1,1000000)/random.randint(1,1000)
    print ("Число: ", number)
    d = random.randint(1,10)  #input('Введите десятичное число: \n')
    print("Точность: ", 10**-d)
    print("Число с заданной точностью: ", round(number, d))


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def Exp2():
    number = int(input('Введите число :\n'))
    if number == 0:
        return
    list = []
    for i in range(1, number + 1, 1):
        if number % i == 0:
            cnt = 0
            for a in range(1, i + 1):
                if i % a == 0:
                    cnt += 1
            if cnt <= 2:
                list.append(i)
    print(f"Простые множители числа {number} : ", list)


# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
def Exp3():
    list = [int(num) for num in input('Укажите числа через запятую: \n').split(',')]
    new_list = []
    new_list.append(int(list[0]))
    for i in list:
        cnt = 0
        for a in new_list:
            if i == a:
                cnt += 1
        if cnt == 0:
            new_list.append(i)
    print(new_list)


# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
def Exp4():
    d = random.randint(1,10)
    print(f"Рандомная степень k = {d}")
    cnt_koef = d + 1
    list_koef = list([int(random.randint(0,100)) for num in range(1,cnt_koef + 1)])
    print(f"Список рандомных коэффициентов: {list_koef}")
    str_ = ""
    for i in range(len(list_koef), 0, -1):
        koef = list_koef[-i]
        dd = str(i-1)
        if koef != 0:
            if dd == "1":
                str_ += str(koef) + "*x+"
            elif dd == "0":
                str_ += str(koef) + "+"
            else:
                str_ += str(koef) + "*x**" + dd + "+"
    with open('Lesson_4_Exp4.txt', 'w+', encoding='utf-8') as file:
        file.write(f"k = {d} =>     " + str_[:-1])
    with open('Lesson_4_Exp4.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print("Читаем из файла: \n", line)
