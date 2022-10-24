#Даны два файла, в каждом из которых находится запись многочлена.
#Задача - сформировать файл, содержащий сумму многочленов.


file1 = open("1_","r")
equation1 = file1.readline()

file2 = open("2_","r")
equation2 = file2.readline()



print(equation1)
print(equation2)

def createEquation(coefEquation: dict):
    equation = ''
    first = True

    for i in coefEquation.items():
        if first:
            first = False
            if i[1] < 0:
                equation += ' -' + str(abs(i[1])) + 'x^' + str(i[0])
            elif i[1] > 0:
                equation += str(abs(i[1])) + 'x^' + str(i[0])
        else:
            if i[1] < 0:
                equation += ' - ' + str(abs(i[1])) + 'x^' + str(i[0])
            elif i[1] > 0:
                equation += ' + ' + str(abs(i[1])) + 'x^' + str(i[0])

    return equation + ' = 0'

def parseEquation(equation: str):
    equation = equation.replace(' + ', ' +').replace(' - ', ' -')
    equation = equation.split()
    equation = equation[:-2]

    dictEquation = {}
    for i in range(len(equation)):
        equation[i] = equation[i].replace('+', '').split('x^')
        dictEquation[int(equation[i][1])] = int(equation[i][0])
    return dictEquation



parEq1 = parseEquation(equation1)
parEq2 = parseEquation(equation2)

resultEquation ={}
for i in range(max(len(parEq1), len(parEq2)), -1, -1):
    first = parEq1.get(i)
    second = parEq2.get(i)
    if first != None or second != None:
        resultEquation[i] = (first if first != None else 0) + (second if second != None else 0)

def printEquation(equation: str):
    return equation.replace(" 1x", "x").replace("x^1", 'x').replace("x^0", '')

result = printEquation(createEquation(resultEquation))


with open('resultEquation.txt', 'w') as file:
    file.write(result)

file1.close() 
file2.close()      


     

