def fib(n):
    first, second = 1, 1
    res = [first, second]

    for i in range(n - 2):
        next_n = first + second
        first = second
        second = next_n
        res.append(next_n)

    return res


def main():
    fib_list = fib(10)
    print(" ".join(str(x) for x in fib_list))
   

if __name__=="__main__":
    main()