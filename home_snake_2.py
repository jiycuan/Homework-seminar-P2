# Задание 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = float(input('Укажите число: '))
summ = 0
str_num = str(num)
str_num = str_num.replace('.', '')
lst_str = list(str_num)
lst_num = map(int, lst_str)
summ = sum(lst_num)
print(summ)


# Задание 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

N = int(input('Укажите число: '))
summ = 1
M = 1

while (M < N + 1):
    summ = M * summ
    M = M + 1
    print(summ)


# Задание 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму, округлённую до трёх знаков после точки.

n = int(input('Укажите число: '))
bill = []
answer = 0

for i in range(1, n + 1):
    current_number = (1 + (1 / i)) ** i
    bill.append(current_number)

for i in range (len(bill)):
    answer += bill[i]

print(round(answer, 3))

# Задание 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на позициях a и b. 
# Значения N, a и b вводит пользователь с клавиатуры.

N = int(input('Укажите число N: '))
a = int(input('Укажите число a: '))
b = int(input('Укажите число b: '))
bill = []
current_number = -N

for i in range (1, N + 1):
    current_number = current_number + 2
    bill.append(current_number)

print(bill)
result = bill[a] * bill[b]
print(result)


# Задание 5. Реализуйте алгоритм перемешивания списка.

import random 
listA = [1, 2, 3, 4, 5, 6] 
random.shuffle(listA) 
print(listA)