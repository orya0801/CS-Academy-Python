def temp_hendler(t, to_celsius):
    if to_celsius:
        temp = temp_to_celsius(t)
    else:
        temp = temp_to_fahrenheit(t)
    
    return temp


def temp_to_celsius(t):
    return (t - 32) * 5 / 9

def temp_to_fahrenheit(t):
    return t * 1.8 + 32


def main():
    t1 = temp_hendler(68, True)
    t2 = temp_hendler(20, False)

    print("68 F = {0} C".format(t1))
    print("{0} F = 20 C".format(t2))

if __name__=="__main__":
    main()
    