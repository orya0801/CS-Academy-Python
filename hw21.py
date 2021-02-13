import itertools


def merge(iter1, iter2):
    lst = list(itertools.chain(iter1, iter2))

    for i in sorted(lst):
        yield i


def main():
    gen = merge((x for x in range(1, 4)), (x for x in range(2, 5)))
    print(list(gen))


if __name__ == '__main__':
    main()
