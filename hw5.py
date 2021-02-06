def get_num_list_from_string(string):
    num_set = set(string.split(' '))
    num_set = [int(i) for i in num_set]

    return num_set

def find_missed_number(num_list):
    for i in range(1, max(num_list)):
        if i not in num_list:
            return i
    
    return max(num_list) + 1

def main():
    string = input("Enter positive numbers with a space: ")
    num_list = get_num_list_from_string(string)
    print(find_missed_number(num_list))

if __name__=="__main__":
    main()