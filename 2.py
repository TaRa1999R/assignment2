print (" LET'S PLAY ROCK, PAPER, SCISSORS ")

import random

player_score = 0
computer_score = 0

print (" Enter rock for ✊ ")
print (" Enter paper for 🖐 ")
print (" Enter scissors for ✌ ")

while player_score < 5 and computer_score < 5 :

    x = random.randint ( 1 , 3 )
    if x == 1 :
        computer_choice = " rock "
    elif x == 2 :
        computer_choice = " paper "
    else :
        computer_choice = " scissors "

    player_choice = input(" Please enter your choice :")

    if computer_choice == " rock " : 
        if player_choice == "paper" :
            print (" 🎉 YOU WIN 🎉 ")
            player_score = player_score + 1
        
        elif player_choice == "scissors" :
            print (" 😜 YOU LOSE 😜 ")
            computer_score = computer_score + 1
        
        elif player_choice == "rock" :
            print (" 😐 EQUAL 😐 ")
        
        else :
            print (" 😵 WRONG WORD 🥴 ")
    
    elif computer_choice == " paper " :
        if player_choice == "scissors" :
            print (" 🎉 YOU WIN 🎉 ")
            player_score = player_score + 1
        
        elif player_choice == "rock" :
            print (" 😜 YOU LOSE 😜 ")
            computer_score = computer_score + 1
        
        elif player_choice == "paper" :
            print (" 😐 EQUAL 😐 ")
        
        else :
            print (" 😵 WRONG WORD 🥴 ")

    elif computer_choice == " scissors " :
        if player_choice == "rock" :
            print (" 🎉 YOU WIN 🎉 ")
            player_score = player_score + 1
        
        elif player_choice == "paper" :
            print (" 😜 YOU LOSE 😜 ")
            computer_score = computer_score + 1
        
        elif player_choice == "scissors" :
            print (" 😐 EQUAL 😐 ")
        
        else :
            print (" 😵 WRONG WORD 🥴 ")
    
    print (" 💻 : ", computer_choice)
    print (" 🧑 : ", player_choice)
    print (" computer score :", computer_score, " VS. player score :", player_score)

if player_score == 5 :
    print (" 🎉🎉CONGRATULATION, YOU WIN THE BATTLE 🎉🎉 ")

elif computer_score == 5 :
    print (" 😜😜 SORRY, YOU LOST THE BATTLE 😜😜 ")

    