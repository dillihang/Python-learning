def squared(text,numb):

    sqrnumb = numb*numb
    
    i=0 
    temptext=""
    position=0

    while i<sqrnumb:
        
        temptext+=text[position:i+1]
        
        i+=1
        position+=1
        
        if len(temptext)==sqrnumb:
            break

        if i==len(text):
            i=0
            position=0
 
    #print(temptext)


    finaltext=""

    t=1
    pos=0

    while t<=numb:
        
        finaltext=temptext[pos*numb:t*numb]

        print(finaltext)   

        pos+=1        
        t+=1



squared("ab", 3)
print()
squared("aybabtu", 5)
