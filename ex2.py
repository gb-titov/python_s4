# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def get_factors(n):
    factor = 2
    lst = []
    while n > 1:
        if(n % factor == 0):
            lst.append(factor)
            n /= factor
        else:
            factor += 1
    return lst

num = int(input('Введите число: '))

print(f'{num} => {get_factors(num)}')