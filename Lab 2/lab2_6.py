number = int(input("Число >>"))

first = 0
second = 1
interation = 0

while (interation < number):
    num = second + first
    first = second
    second = num
    print(num, end=" ")
    interation += 1
    