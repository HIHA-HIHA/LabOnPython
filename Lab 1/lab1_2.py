numberX = float(input("Число X >>"))

function = 0
if(numberX+5 == 0):
    print("Невозможное число X: производиться деление на 0")
else:
    function = (numberX ** 3)/(2*(numberX+5))
    print(f"Значение функции (x ** 3)/(2*(x+5)) = {function}")