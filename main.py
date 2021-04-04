import pywhatkit as pw

choice = 'y'

phone_number = []
while choice == 'y':
    phone_number += [input("Enter the Phone Number: \n")]
    choice = input("Do you want to enter another phone number ? y/n \n")
    
msg = input("Enter the Message: \n")

time_hour = int(input("Hour : \n"))
time_minute = int(input("Minute : \n"))

j = 0
for i in phone_number:
    
    if time_minute >= 60:
        time_minute -= 60
        time_hour += 1
        
    pw.sendwhatmsg(i, msg, time_hour, time_minute + j )

    j += 1
