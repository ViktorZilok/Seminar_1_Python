#Сформировать список из  N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81 и т.д.

number = int(input('Введите число: '))

def kit_numbers(N):
    return [((-3)**i) for i in range(N)]

print (kit_numbers(number))

#Пользователь задаёт две строки. Определить количество вхождений одной строки в другой. https://pythonist.ru/python-poisk-v-stroke/

str1 = input('Задайте первую строку: ')
str2 = input('Задайте вторую строку: ')
n = 0

for i in range(len(str1) - len(str2) + 1):
    if str1[i:i + len(str2)] == str2:
        n += 1
print(f'Количество вхождений {n}')
print(str1)
print(str2)

# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]


def factor(N):
    number_one = 1
    for i in range(N):
        number_one *= i + 1
        print(number_one)


factor(4)


# Подсчитать сумму цифр в вещественном числе.


from random import uniform

n = round(uniform(1, 100), 3)


def sum_digit(n):

    return sum(map(int, list(str(n).replace('.', ''))))


print(n)
print(sum_digit(n))
