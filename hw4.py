import re

def get_numbers_from_string(string):
    # Находим все подстроки, удовлятворяющие паттерну: 
    # Подстрока начинается с -, + или пустого значения,
    # а затем идет последовательность из цифр
    nums = re.findall(r'[-+]?\d+', string)
    # Переводим все элементы списка из строки в числа
    nums = [int(i) for i in nums]

    return nums

def count_sum(num_list):
    sum = 0

    for el in num_list:
        sum += el

    return sum

def main():
    string = input()
    num_list = get_numbers_from_string(string)
    print(count_sum(num_list))


if  __name__=="__main__":
    main()