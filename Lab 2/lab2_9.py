import random
secret = random.randrange(0, 100)


print("Загадано числа от 1 до 100")
attempts = 0
while (attempts < 10):
    userInput = int(input("Целое число >>"))
    if (userInput < secret):
        print("Число меньше загаданного")
    elif(userInput > secret):
        print("Число больше загаданного")
    elif (userInput == secret):
        print("Число угадано")
        break
    
    
    attempts +=1
    print(f"Осталось попыток: {10-attempts}")

print(secret)