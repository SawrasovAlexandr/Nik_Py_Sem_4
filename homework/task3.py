# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint


def del_dubl(row: list) -> list:
    result = []
    for i in range(len(row)):
        temp = row.pop(i)
        if not temp in row:
            result.append(temp)
        row.insert(i, temp)
    return result


def main():
    numbers = [randint(0, 9) for _ in range(randint(10, 20))]
    print(numbers)
    print(del_dubl(numbers))


if __name__ == '__main__':
    main()


