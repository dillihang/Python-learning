numb = 0

while numb<10:
    numb+=1
    if numb%2==1:
        print(numb)


#odd or even numbers

print("Are you ready?")
number = int(input("Please type in a number: "))
while number !=0:
    number-=1
    print(number)
print("Now!")



numbers=0
print("Are you ready?")
numbers = int(input("Please type in a number: "))
while True:
    numbers-=1
    if numbers==0:
        break
    
    print(numbers)
print("Now!")


a = int(input("Please enter a number: "))
i=1
print("upper limit: " + str(a))
while a>i:
    print(i)
    
    i+=1

