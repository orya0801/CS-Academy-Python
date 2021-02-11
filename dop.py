def n_arr(lst):
    for elem in enumerate(lst):
        if elem[0] == 0:
            final_list = ["" for _ in range(elem[1])]
        else:
            final_list = [final_list for _ in range(elem[1])]

    return final_list


def main():
    print(n_arr([2, 2]))
    print(n_arr([2, 2, 2]))


if __name__ == '__main__':
    main()
