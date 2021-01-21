def get_num_list_from_string(string):
    num_set = set(string.split(' '))
    num_set = sorted([int(i) for i in num_set])

    return list(num_set)

def find_missed_number(num_list):
    for i in range(num_list[0], num_list[-1]):
        if i not in num_list:
            return i

def main():
    string = input()
    num_list = get_num_list_from_string(string)
    print(find_missed_number(num_list))

if __name__=="__main__":
    main()