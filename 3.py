print (" 🧮 CALCULATE STUDENT'S AVERAGE SCORE 🧮 ")
print (" Please enter student's score as input ")
print (" Please enter 'exit' as input to see the average as result ")

sum = 0 
n = 0 

while True :
    vurudi = input (" Please enter the input : ")

    if vurudi == "exit" :
        break

    else :
        score = float ( vurudi )
        sum = sum + score
        n = n + 1
  
average = sum / n
print (" The average score is ", average)
print (" YOUR WELCOM ")