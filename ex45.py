import random
import re


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


def read_from_file(file_name):
    f = open(file_name, 'r')
    res = f.readline()
    f.close() 
    return res


def sum_pol(pol1, pol2):
    dict1 = pol_2_dict(pol1)
    dict2 = pol_2_dict(pol2)
    dic = dict1.copy()
    dic.update(dict2)
    str = []
    for key in dic:
        if dict1.get(key) != None and dict2.get(key) != None:
            dic[key] += dict1[key]
        if key > 1:
            str.append(f'{dic[key]}x^{key}')
        elif key == 1:
            str.append(f'{dic[key]}x')
        else:
            str.append(f'{dic[key]}')
    return '+'.join(str)


def pol_2_dict(str):
    lst = str.split('+')
    dict = {}
    for i in lst:
        if(re.match('^\d*x\^\d*', i)):
            res = re.split('x\^', i)
            dict[int(res[1])] = int(res[0])
        elif (re.match('^\d*x', i)):
            res = re.split('x', i)
            dict[1] = int(res[0])
        else:
            dict[0] = int(i)
    return dict
