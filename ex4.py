# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import random

def create_polinomial(k):
    coef = random.sample(range(0, 99), k + 1) 
    lst = []
    while k >= 0:
        if coef[k] == 0:
            k-=1
            continue
        elif k > 1:
            lst.append(f'{coef[k]}x^{k}')
        elif k == 1:
            lst.append(f'{coef[k]}x')
        else:
            lst.append(f'{coef[k]}')
        k-=1
    return '+'.join(lst)


def save_2_file(fileName, str):
    f = open(fileName, 'w')
    f.write(str)
    f.close() 
        
        
k = int(input("Введите коэффициент: "))
file = 'ex4.txt'
pol = create_polinomial(k)

print('Сформированный многочлен: ' + pol)
print('Сохраняю в файл: ' + file)
save_2_file(file, pol)
print('Данные сохранены.')


