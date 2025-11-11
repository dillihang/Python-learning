def spruce(tall):
    
    i = 0

    space1=tall-1
    space=" "*space1
    laststar=space
    star="*"

    

    print("a spruce!")
    
    while i < tall:   

        
        space+=star 
             

        print(space)

        i+=1

    
    
    print(laststar+"*")



spruce(3)
print()
spruce(5)