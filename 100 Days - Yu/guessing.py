from random import randint

computer = randint(1,10)

user = int(input("Guess a number between 1 and 10: "))

while user != computer:
    if user > computer:
        user = int(input("Too high, try again: "))
    elif user < computer:
        user = int(input("Too low, try again: "))

print("You win!")