print (" Guess Number 🤔🧐 ")

import random

computer_number = random.randint ( 0 , 100 )
guess = 1
print (" The number can be varied from 0 to 100 ")

while True :
    user_number = int ( input (" Please enter your guess : "))
    if user_number == computer_number :
        print (" 🎉 CONGRATULATION 🎉")
        print (" 🎉 YOU WIN 🎉 ")
        print (" The number was ", computer_number)
        print (" It was your ", guess, "guess ")
        break

    elif user_number < computer_number :
        print (" Peak higher number ⬆ ")
        guess = guess + 1

    else :
        print (" Peak lower number ⬇ ")
        guess = guess + 1