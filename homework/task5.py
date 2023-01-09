# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов

from random import randint
from task4 import *

def file_read(file: str) -> str:
    with open(file, 'r', encoding='UTF-8') as data:
        return data.readline()

def normalscript(num: str) -> str:
    sup = '⁰¹²³⁴⁵⁶⁷⁸⁹'
    result = ''
    for temp in num:
            for i in range(len(sup)):
                if temp == sup[i]: result += str(i)
    return result

def pars_polinom(polinom: str) -> dict:
    result = {}
    polinom = polinom.replace(' ','').replace('=0', '').replace('*', '').split('-')
    polinom = '+-'.join(polinom).split('+')
    if polinom[0] == '': polinom.pop(0)
    for temp in polinom:
        i = temp.find('x')
        if i == len(temp) - 1: 
            if len(temp) == 2 and not temp[0].isdigit(): result[1] = -1
            elif temp == 'x': result[1] = 1
            else: result[1] = int(temp[:i])
        elif i == 0: result[int(normalscript(temp))] = 1
        elif i == 1 and not temp[0].isdigit(): result[int(normalscript(temp[1:]))] = -1
        elif i == -1: result[0] = int(temp)
        else: result[int(normalscript(temp[i:]))] = int(temp[:i])
    return result

def sum_polinom(pol_1: str, pol_2: str) -> str:
    pol_dict_1 = pars_polinom(pol_1)
    pol_dict_2 = pars_polinom(pol_2)
    sum_keys = set(pol_dict_1.keys())
    sum_keys.update(pol_dict_2.keys())
    sum_dict = {}
    for key in sum_keys:
        sum_dict[key] = str(pol_dict_1.get(key, 0) + pol_dict_2.get(key, 0))
    sum_keys = list(sum_keys)
    sum_keys.sort(reverse=True)
    result = []
    for key in sum_keys: 
        if sum_dict[key] == '0': continue
        elif sum_dict[key] == '1': value = ''
        elif sum_dict[key] == '-1': value = '-'
        else: value = sum_dict[key] + '*'
        if key == 0: result.append(sum_dict[key])
        elif key == 1: result.append((value) + 'x')
        else: result.append((value) + 'x' + superscript(key))
    result = ' + '.join(result).split('+ -')
    result = '- '.join(result) + ' = 0'
    return result


def main():
    file_write(get_polinom(randint(5,12), -5, 5), 'poli_1.txt')
    file_write(get_polinom(randint(5,12), -5, 5), 'poli_2.txt')
    poli_1 = file_read('poli_1.txt')
    poli_2 = file_read('poli_2.txt')
    poli_sum = sum_polinom(poli_1, poli_2)
    file_write(poli_sum, 'poli_sum.txt')

    # print(poli_1)
    # print(poli_2)
    # print(poli_sum)
    

if __name__ == '__main__':
    main()