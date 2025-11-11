import math

i=0
x=0
n=0
p=0
mean=0
while True:
    numbers = int(input("Please enter a number, enter 0 to stop: "))
    if numbers == 0:
        break
    i+=1
    x+=numbers
    mean=x/i
    if "-" in str(numbers):
        n+=1
    else:
        p+=1


print("You have typed in " + str(i) + " numbers")
print("The sum of the numbers are " + str(x)) 
print("The mean of the number is " + str(mean))
print("negative numbers " + str(n))
print("posetive numbers " + str(p))
