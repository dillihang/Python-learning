import datetime

day=int(input("Day: "))
month=int(input("Month: "))
year=int(input("Year: "))

person = datetime.datetime(year, month, day)
millennium_eve = datetime.datetime(1999, 12, 31)

difference = millennium_eve - person

if difference.days < 0:

    print("You weren't born yet on the eve of the new millennium")
    
else:
    print(f"You were {difference.days} old on the eve of the new millennium")

    