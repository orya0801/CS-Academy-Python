def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False


def main():
    sum = 0 

    for i in range(1, 1000000):
        if is_palindrome(str(i)) and is_palindrome("{0:b}".format(i)):
            sum += i
        
    print("sum = {}".format(sum))


if __name__=="__main__":
    main()


# sum = 872187