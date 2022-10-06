# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$
import math


def get_pi(d):
    ndigits = 0
    
    while d < 1:
        d *= 10
        ndigits += 1
    return round(math.pi, ndigits)


num = float(input('Введите точность числа Пи, например, 0.001: '))
print(f'π = {get_pi(num)}')   
     