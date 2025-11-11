while True:

    numb = int(input("Please enter a number, 0 or -1 will end: "))
    if numb==0 or numb<0:
        print("Thanks and bye!")
        break

    low=1
    high=numb

    while low<=high:
        print(low)
        if low!=high:
            print(high)
        low+=1
        high-=1

        

   
 