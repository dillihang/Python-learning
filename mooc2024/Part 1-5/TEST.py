year = int(input("Please enter a year: "))

if year % 4 ==0:
    if year % 100 == 0: 
        if year % 400 == 0:
            print("that year is a leap year")
        else:
            print("that year is not a leap year")
    else:
        print("that year is a leap year")
else:
    print("that year is not a leap year")

#     Generally, any year that is divisible by four is a leap year. However, if the year is additionally divisible by 100, it is a leap year only if it also divisible by 400.

# Please write a program which asks the user for a year, and then prints out whether that year is a leap year or not (NESTED).