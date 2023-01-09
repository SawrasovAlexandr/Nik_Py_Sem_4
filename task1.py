# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

def find_min_max(list_num):
    min_num = int(list_num[0])
    max_num = int(list_num[0])
    for num in list_num:
        num = int(num)
        if max_num < num:
            max_num = num
        if min_num > num:
            min_num = num
    return max_num, min_num


def main(): #тело программы
    list_num = input('Введите числа через пробел ->').split()
    print(*find_min_max(list_num))

if __name__ == "__main__":
	main()
