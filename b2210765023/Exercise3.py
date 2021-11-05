import random
number = random.randint(1,50)

while True :
    x = int(input("Please guess the number: "))
    if x<number :
        print("Increase your guess")
    elif x>number :
        print("Decrease your guess")
    else:
        print("Your guess is correct")
        break


