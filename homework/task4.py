# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint


def superscript(num: int) -> str:
    sup = '⁰¹²³⁴⁵⁶⁷⁸⁹'
    num = str(num)
    result = ''
    for temp in num:
            result += sup[int(temp)]
    return result

def get_polinom(degree: int, min: int = 0, max: int = 100) -> str:
    polinom = ''
    for i in range(degree, -1, -1):
        arg = randint(min, max)
        if arg == 0: continue
        elif arg > 1: arg = '+ ' + str(arg) + '*x'
        elif arg == 1: arg = '+ x'
        elif arg == -1: arg = '- x'
        elif arg < -1: arg = '- ' + str(abs(arg)) + '*x'
        if i > 1: polinom += arg + superscript(i) + ' '
        elif i == 1: polinom += arg + ' '
        else: # i == 0
            if arg in ('+ x', '- x'): polinom += arg.replace('x', '1') + ' '
            else: polinom += arg.replace('x', '').replace('*', '') + ' '
    if polinom.startswith('+'): polinom = polinom[2:] + '= 0'
    else: polinom = '-' + polinom[2:] + '= 0'
    return polinom

def file_write(text: str, file: str = 'file.txt') -> None:
    with open(file, 'w', encoding='UTF-8') as data:
        data.write(text)


def main():
    k = input('Введите степень многочлена: ')
    while not k.isdigit():
        k = input('Степень должна быть натуральным числом: ')
    file_write(get_polinom(int(k)), 'poli.txt')
   

if __name__ == '__main__':
    main()