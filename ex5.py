# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

from ex45 import *
import re

f_file = 'ex5_1.txt'
s_file = 'ex5_2.txt'

# формируем два файла
save_2_file(f_file, create_polinomial(3))
save_2_file(s_file, create_polinomial(2))

# читаю два файла
str = read_from_file(f_file)
str2 = read_from_file(s_file)

# суммирую полиномы
res = sum_pol(str, str2)

print(f'{str} + {str2} = {res}')

save_2_file('ex5_sum.txt', res)        
