import operator

def num_translate_adv(number = ""):
    number_ = number.lower()
    dict = {
        "один":"one"
        ,"два":"two"
        ,"три":"three"
        ,"четыре":"four"
        ,"пять":"five"
        ,"шесть":"six"
        ,"семь":"seven"
        ,"восемь":"eight"
        ,"девять":"nine"
        ,"десять":"ten"
    }
    print(dict.get(number_, "none").title() if number[0].isupper() else dict.get(number_, "none"))

def thesaurus_adv(names = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"]):
    jsonfile = []
    list_letter = []
    dict_name = {}

    for r in names:
        letter = r.split()[1][0].title()

        if letter not in list_letter:
            list_letter.append(letter)
            list_letter_ = []
            dict_name_ = {}
            names_2 = [i for i in names if letter == i.split()[1][0].title()]

            for rr in names_2:
                letter_ = rr.split(",")[0][0].title()

                if letter_ not in list_letter_:
                    list_letter_.append(letter_)
                    dict_name_[letter_] = [i for i in names_2 if letter_ == i.split()[0][0].title()]

            dict_name[letter] = dict_name_ #dict(sorted(dict_name_.items(), key = operator.itemgetter(0)))

    print(dict(sorted(dict_name.items(), key = operator.itemgetter(0))))

