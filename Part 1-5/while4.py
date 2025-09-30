Lyear = int(input("Please enter a year: "))
LeapYear=Lyear

while True:
    LeapYear += 1  # check the next year
    # Check if Lyear is a leap year
    if (LeapYear % 4 == 0 and LeapYear % 100 != 0) or (LeapYear % 400 == 0):
        break

print("The next leap year after " + str(Lyear) + " is " + str(LeapYear))



    

    
   