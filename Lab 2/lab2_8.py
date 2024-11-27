number1 = int(input("Целое число 1 >>"))
number2 = int(input("Целое число 2 >>"))

while number1 != 0 and number2 != 0:
    if number1 > number2:
        number1 = number1 % number2
    else:
        number2 = number2 % number1

print(number1 + number2)
