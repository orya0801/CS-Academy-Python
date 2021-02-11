def create_list_from_string(string):
    curr_word = ""
    final_list = []

    for ch in string:
        if ch != " ":
            curr_word += ch
        elif curr_word not in final_list:
            final_list.append(curr_word)
            curr_word = ""
        else:
            curr_word = ""

    return ' '.join(final_list)


def main():
    string = input("Enter text: ")
    print(create_list_from_string(string))


if __name__ == "__main__":
    main()
