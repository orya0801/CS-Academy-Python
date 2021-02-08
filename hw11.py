import string 

CHARS = string.ascii_lowercase


def letters_range(start, stop, step=1):
    start_i = CHARS.index(start)
    stop_i = CHARS.index(stop)

    return list(CHARS[start_i:stop_i:step])


def main():
    print(letters_range('b', 'w', 2))
    print(letters_range('a', 'g'))
    print(letters_range('g', 'p'))
    print(letters_range('p', 'g', -2))
    print(letters_range('a', 'a'))

    
if __name__=="__main__":
    main()