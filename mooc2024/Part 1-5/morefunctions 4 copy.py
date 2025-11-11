def spruce(height):

    length="**"

    i=0

    star="*"
    space=" "
    numberofspaces=height-1
    end=height-1 

    
    while i<height:
        
        print((space * numberofspaces) + star)

        star+=length
        numberofspaces-=1
        i+=1
    
    
    print((space * end) + "*")



spruce(3)
print()
spruce(5)
print()
spruce(6)
print()
spruce(33)

