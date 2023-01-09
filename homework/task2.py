# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

from random import randint

def prime_factors(num: int) -> list:
    temp = num
    result = []
    while temp > 1:
        for i in range(2, int(temp ** 0.5) + 1):
            if temp % i == 0:
                temp //= i
                if not i in result:
                    result.append(i)
                break
        else: 
            if not temp in result:
                result.append(temp)
            temp = 1
    return result


def main():
    number = randint(1, 10 ** 15)
    print(f'Простые множители числа {number}: {prime_factors(number)}')


if __name__ == '__main__':
    main()

