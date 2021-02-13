def text_handler():
    string = input("-> ")

    if string == "cancel":
        print("Bye!")
    else:
        try:
            if (x := int(string)) % 2 == 0:
                print(x // 2)
            else:
                print(x * 3 + 1)
        except ValueError:
            print("Не удалось преобразовать введенный текст в число.")
        finally:
            return text_handler()


def main():
    text_handler()


if __name__ == "__main__":
    main()
