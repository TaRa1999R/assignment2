print (" TRANSFER SECOND TO TIME ")
print (" Please enter the seconds as input ")

minute = 00
hour = 00
second = int ( input (" please enter the input : "))

if second >= 3600 :
    hour = int ( second / 3600 )
    print (hour)

    second = second - ( hour * 3600 )
    print(second)

    if second >= 60 :
        minute = int ( second / 60 )
        print (minute)

        second = second - ( minute * 60 )
        print (second)

elif 3600 > second >= 60 :
    minute = int ( second / 60 )
    print (minute)

    second = second - ( minute * 60 )
    print (second)

print (" output is = ", hour, ":", minute, ":", second)