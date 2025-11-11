while True:

    numb = int(input("Please enter a number, 0 or -1 will end: "))
    if numb==0 or numb<0:
        print("Thanks and bye!")
        break

    i=1
    result=1

    while i<=numb:
   
        result*=i
        
        i+=1
    print(f"The Factorial of the number {numb} is {result}")