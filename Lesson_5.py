# Задание 1
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
def Exp1():
    del_word = 'абв'
    result = ' '.join([word for word in input('Введите через пробелы слова: \n').split() if del_word not in word])
    print(result)


# Задание 4
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# import collections
# d = collections.defaultdict(int)
# for c in 'fff dddd bbbb aaa':
#     d[c] += 1
# print(d)
def Exp4(type = 0, string = ''):
    #type = 0  -- сжатие        Exp4(0, 'fff dddd bbbb aaa')
    #type = 1  -- распаковка    Exp4(1, '3f 4d 4b 3a')
    if type == 0:
        count = {}
        for s in string.split(): #'fff dddd bbbb aaa'
          for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        ss = ''
        for key in count:
            ss = ss + f'{count[key]}{key}' + ' '
        print(ss[:-1])
    else:
        list = []
        for s in string.split(): #'3f 4d 4b 3a'
            cnt = ''
            chr = ''
            for i in s:
                if i.isdigit():
                    cnt += i
                else:
                    chr += i
            list.append(chr*int(cnt))
        print(' '.join(list))

# Задание 2
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
def Exp2():
    import random
    #print("\033[H\033[J", end="")
    players = {}
    i = int(input("Укажите кол-во конфет, больше 29:\n"))
    players[1] = input("Укажите свой ник:\n")
    players[2] = "Ботяра"   #input("Укажите ник:\n")
    start_player = random.randint(1,2)
    print(f"Начинает игрок {players[start_player]}\n")
    if start_player == 2:
        number = i % (28 + 1)
        print(players[2], "выбирает", number)
    else:
        number = int(input(f"{players[start_player]} укажи число конфет, которое возьмешь, но не больше 28:\n"))
        if number > 28:
            print("Кривой, нужно выбирать небольше 28!\nИгра окончена!")
            return
    i = i - number
    print("Осталось", i, "конфет\n")
    id_player = start_player
    while i > 0:
        #print("\033[H\033[J", end="")
        if i > 28:
            if id_player == 1:
                id_player = 2
                number = i % (28 + 1) #number = int(input(f"{players[id_player]} укажи число конфет, которое возьмешь, но не больше 28:\n"))
                print(players[2], "выбирает", number)
            else:
                id_player = 1
                #number = i % (28 + 1)
                number = int(input(f"{players[id_player]} укажи число конфет, которое возьмешь, но не больше 28:\n"))
                if number > 28:
                    print("Кривой, нужно выбирать небольше 28!\nИгра окончена!")
                    return
                print(players[1], "выбирает", number)
            i -= number
            print("Осталось", i, "конфет\n")
        else:
            if id_player == 1:
                print(f"Выиграл {players[2]}!")
            else:
                print(f"Выиграл {players[1]}!")
            break
