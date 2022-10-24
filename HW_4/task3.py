#3.Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
#исходной последовательности.
#Пример:
#47756688399943 -> [5]
#1113384455229 -> [8,9]
#1115566773322 -> []

from random import randint as rI

unique ={}

myList = ''.join(list(map(str,[rI(0,9) for i in range(20)]))) 


for num in myList:
    unique[num] = unique.get(num, 0) + 1


uList = []

for i in unique.items():
    if i[1] == 1:
        uList.append(i[0])

print(f'{myList} => {uList}')



