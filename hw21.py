def merge(iter1, iter2):
    try:
        buf1 = next(iter1)
    except StopIteration:
        yield from iter2

        return

    try:
        buf2 = next(iter2)
    except StopIteration:
        yield buf1
        yield from iter1

        return

    while True:
        if buf1 < buf2:
            yield buf1

            try:
                buf1 = next(iter1)
            except StopIteration:
                yield buf2
                yield from iter2

                break

        else:
            yield buf2

            try:
                buf2 = next(iter2)
            except StopIteration:
                yield buf1
                yield from iter1

                break


def main():
    print(list(merge((x for x in range(1, 5)), (x for x in range(2, 6)))))
    print(list(merge((x for x in range(1, 1)), (x for x in range(2, 6)))))
    print(list(merge((x for x in range(1, 5)), (x for x in range(2, 2)))))
    print(list(merge((x for x in range(1, 10)), (x for x in range(2, 5)))))


if __name__ == '__main__':
    main()
