while True:

    numb = int(input("Please enter a number, 0 or -1 will end: "))
    if numb==0 or numb<0:
        print("Thanks and bye!")
        break

    i=1
   

    while i<=numb:
        
        if i%2==0:
            print(f"{i}")
        
            t=i
          
            print(f"{t-1}")        
        
        i+=1

    if t<numb:
                print(numb)
 