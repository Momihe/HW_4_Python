# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
import random
list_1_len = int(input('Введите длинну первого массива: '))
list_2_len = int(input('Введите длинну второго массива: '))
list_1 = [random.randint(-10,10) for i in range(list_1_len) ]
list_2 = [int(input(f'Введите {i+1}-й элемент массива: ')) for i in range(list_2_len)]
list_3 = set()
list_4 = []
print(list_1)
print(list_2)
for i in list_1: list_3.add(i)
for i in list_2: list_3.add(i)
# list_4 = range(len(list_3))
for i in list_3:
    list_4.append(i)
i = 0
while i < len(list_4) - 1:
    j = 0
    while j < len(list_4) - 1:
        if list_4[j] > list_4[j + 1]:
            z = list_4[j + 1]
            list_4[j + 1] = list_4[j]
            list_4[j] = z
        else: j += 1
    i +=1 
print(list_4)


    

