def create_list_from_string(string):
    wlist= string.split(' ')
    final_list = []

    for el in wlist:
        if el not in final_list:
            final_list.append(el)

    return ' '.join(final_list)


def main():
    string = input()
    print(create_list_from_string(string))

if __name__=="__main__":
    main()