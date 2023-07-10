print (" FIBONACCI SEQUENCE ")

n = int ( input(" enter the number of Fibonacci sequence you want me to show : "))
a = 0
b = 1

if n <= 0 :
    print (" ❌ Incorrect number ❌ ")

if n >= 1 :
    print ( a )

if n >= 2 :
    print ( b )

if n >= 3 :
    for i in range ( 2 , n ) :
        c = a + b 
        a = b
        b = c
        print ( b )