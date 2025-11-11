from math import sqrt

while True:

    number = int(input("Please enter the number: "))
    if number<=0:
        break
    print("The answer is " + str(float(sqrt(number))))

print("Invalid Number")