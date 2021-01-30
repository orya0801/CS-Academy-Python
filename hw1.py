'''
    Класс bool() возвращает логическое значение указанного объекта,
    True или False. Соответствие объектов int и str с bool:
    1. Для int: 0 = False. Для всех остальных значений int - True.
    2. Для str: "" (пустая строка) = False. Для всех остальных значений str - True.
'''

print(bool(0)) # False
print(bool("")) # False
print(bool(-15)) # True
print(bool("Hello!")) # True

'''
    В Python 2:
    1. raw_input() - используется для получения ввода от пользователя через командную строку
    2. input()     - анализирует строку и пытается запустить как код Python

    В Python 3: 
    1. raw_input() был убран из Python3. Аналогом данной функции в python 3 является:
        eval(input())
    2. input() - используется для получения ввода пользователя с клавиатуры

'''

eval(input()) # print('Hello, World!') -> Hello, World!


'''
    Главным отличием между print в Python 2 и Python 3 закллючается в том,
    что в Python 2 print был оператором, а в третьей версии этот оператор был
    заменен на функцию print().

    Например:
    Python2: print "The answer is", 2*2
    Python3: print("The answer is", 2*2)
'''