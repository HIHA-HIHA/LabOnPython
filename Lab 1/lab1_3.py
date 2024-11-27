import math
numberA = float(input("Число A >>"))
numberB = float(input("Число B >>"))
numberC = float(input("Число C >>"))

discriminant = (numberB ** 2)-(4 * numberA * numberC)
if(discriminant > 0):
    numberX1 = (-numberB - math.sqrt(discriminant))/(2*numberA)
    numberX2 = (-numberB + math.sqrt(discriminant))/(2*numberA)
    print(f"Решение квадратного уравнение: x1 = {numberX1}, x2 = {numberX2}, Дискриминант = {discriminant}")
else:
    print("Дискриминант меньше 0")
