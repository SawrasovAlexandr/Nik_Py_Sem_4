# Вычислить число c заданной точностью d

# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from decimal import *


def main():
    num = input('Введите число: ')
    d = int(input('Введите количество знаков после запятой: '))
    d = '1.' + '0' * d
    result = Decimal(num).quantize(Decimal(d), ROUND_HALF_UP)
    print(result)
           

if __name__ == '__main__':
    main()