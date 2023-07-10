print (" 🎲 ROLLING DICE SIMULATING 🎲 ")
print (" 6 has prize ")

import random

dice_number = random.randint ( 1 , 6 )
print (" 🎲 : ", dice_number )

while dice_number == 6 :
    dice_number = random.randint ( 1 , 6 )
    print (" 🎁 :", dice_number)