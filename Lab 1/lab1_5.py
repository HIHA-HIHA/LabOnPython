angle1 = float(input("Угол 1 >>"))
angle2 = float(input("Угол 2 >>"))

if(angle1+angle2 >= 180):
    print("Данного треугольника не существует")
else:
    if(angle1 == 90 or angle2 == 90):
        print("Данный треугольник прямоугольный")
    else:
        print("Данный треугольник не прямоугольный")
