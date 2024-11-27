temperature = float(input("Температура воды >>"))
if temperature < 0:
    print("Состояние воды: твёрдое")
elif temperature < 100:
    print("Состояние воды: жидкое")
else:
    print("Состояние воды: газообразное")