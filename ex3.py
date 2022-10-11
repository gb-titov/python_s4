# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst = [6, 2, 3, 74, 5, 2, 61, 5, 6, 1]

def get_uniq(lst):
    new_lst = []
    for i in lst:
        if(lst.count(i) == 1):
            new_lst.append(i)
    return new_lst


print(f'{lst} => {get_uniq(lst)}')
