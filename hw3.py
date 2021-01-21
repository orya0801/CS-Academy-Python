def get_dict(string):
    # Cписок всех слов строки
    wlist = string.split(' ')
    # Список уникальных слов строки
    wset = set(wlist)

    wdict = {}
    # Счетчтик максимального количества повторений слова в строке
    max_count = 0

    for word in wset:
        count = wlist.count(word)

        if count > max_count:
            max_count = count

        wdict.update({word:count})

    return (wdict, max_count)

def print_result(wdict, max_count):
    for v, k in wdict.items():
        if k == max_count:
            print("{0} - {1}".format(k, v))

def main():
    string = input()
    wdict, max_count = get_dict(string)
    print_result(wdict, max_count)

if __name__=="__main__":
    main()