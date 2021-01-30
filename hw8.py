def parse(string, i=0):
    if len(string) > i:
        return string[i] + parse(string, i + 1)
    

def main():
    string = input()
    print(parse(string))
    


if __name__=="__main__":
    main()