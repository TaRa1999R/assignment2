print (" TRANSFER TIME TO SECOND ")
print (" Please enter the time by the form of hhmmss ")
print (" h for hour ")
print (" m for minute ")
print (" s for second ")

time = int ( input (" Please enter the time : "))

hour = int ( time / 10000 )
second = hour * 3600

time = time - ( hour * 10000 )

minute = int ( time / 100 )
second = second + ( minute * 60 )

time = time - ( minute * 100 )

second = second + time 

print (" time in seconds is equal to = ", second)
