import math
# problem 6
# Find the difference between the sum of the squares 
# of the first one hundred natural numbers and the square 
# of the sum.
#
# Answer = 25164150
print(sum(range(1, 101))**2 - sum(x**2 for x in range(1, 101)))

# problem 9
# There exists exactly one Pythagorean triplet for which 
# a + b + c = 1000.
# Find the product abc.
#
# Answer: 200*375*425=3187500
print([a * b * (1000 - a - b) for a in range(1, 400) for b in range(a+1, 400) if a**2 + b**2 == (1000 - a - b)**2][0])


# problem 40
# Champernowne's constant
#
# Answer = 210

# Подсчитываем количество итераций необходимых для составления числа
iter_count = sum(9*(x+1) * pow(10, x) for x in range(6))
# Составляем строку-число
number = ''.join([str(x) for x in range(1, iter_count)])
# Выбираем 10, 100, 1000, 10000, 100000, 1000000 элементы и перемножаем их
print(math.prod([int(number[10**x-1]) for x in range(0, 7)]))


# problem 48
# Find the last ten digits of the series,
#  1^1 + 2^2 + 3^3 + ... + 1000^1000.
#
# Answer = 9110846700
print(sum(x**x for x in range(1, 1001))%(10**10))