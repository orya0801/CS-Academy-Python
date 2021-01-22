def collatz(num):
    count = 0

    while num != 1:
        count += 1 
        if num % 2 == 1:
            num = num * 3 + 1
        else:
            num /= 2
    
    return count


def main():
    print(collatz(12)) # 9 шагов
    print(collatz(15)) # 17
    print(collatz(100)) # 25


if __name__ == "__main__":
    main()