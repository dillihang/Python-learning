import datetime

"""
Record daily screen time for TV, computer, and mobile devices.
Calculates total and average minutes over a specified period.
Saves the results to a file in a readable format with dates and daily breakdowns.
"""

mydate_dict={}

file_name=input("Filename: ")

while True:
    start_date=input("Starting date: ")

    try:
        datepart=start_date.split(".")

        dd=int(datepart[0])
        mm=int(datepart[1])
        yyyy=int(datepart[2])

        actual_start_date=datetime.datetime(yyyy,mm,dd)
        break # valid date entered
    except (ValueError, IndexError):
        print("Invalid date. Please enter a correct date in format dd.mm.yyyy.")


how_days=int(input("How many days: "))


print("Please type in screen time in minutes on each day (TV computer mobile): ")
for i in range(how_days):

    my_date=actual_start_date+datetime.timedelta(days=i)
    minutes=input(f"screen time {my_date.strftime("%d.%m.%Y")}: ")

    mydate_dict[my_date.strftime("%d.%m.%Y")]=minutes

print(f"Data stored in file late_june.txt")

# print(mydate_dict)

date_list=list(mydate_dict.keys())

# print(date_list)

valuestring=""
totalminutes=0

for keys,values in mydate_dict.items():
    valuestring+=values + " "

valuestring=valuestring.strip()
valuepart=valuestring.split(" ")

for items in valuepart:
    totalminutes+=int(items)
    
average = totalminutes/how_days


with open("part7/" + file_name, "w") as file:

    file.write(f"Time period: {date_list[0]} - {date_list[-1]}\n")
    file.write(f"Total minutes: {totalminutes}\n")
    file.write(f"Average minutes: {average:.1f}\n")
    for keys, values in mydate_dict.items():
        if " " in values:
            new_values = values.replace(" ", "/")
            file.write(f"{keys}: {new_values}\n")


    