import random
secret = random.randrange(1, 100)


print("Загадано числа от 1 до 100")

while (True):
    userInput = input("Целое число >>")
    if(userInput == "exit"):
        break
    
    userInput = int(userInput)
    
    if (userInput < secret):
        print("Число меньше загаданного")
    elif(userInput > secret):
        print("Число больше загаданного")
    elif (userInput == secret):
        print("Число угадано")
        break
    