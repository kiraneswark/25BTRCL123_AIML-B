

import random

number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Congratulations! You guessed the correct number.")
else:
    print("Wrong Guess!")
    print("The correct number was:", number)
    
    #sample output
    #Guess a number between 1 and 10: 5     
    #Wrong Guess!
    #The correct number was: 8