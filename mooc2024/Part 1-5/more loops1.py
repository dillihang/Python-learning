sentence = input("Please type in a sentence: ")

char=" "
tempsentence=sentence
t=0    
    
while t<=len(tempsentence):
    i=tempsentence.find(char)
    #print(i)
    #print(tempsentence)
    print(tempsentence[0])
    if i==-1:
        break    
    #print(f"{char} {i}")
    
    if i>=0:
        #print(tempsentence)   
        tempsentence=tempsentence[i+1:]
    
        
    

    
    
    
    #FUCKK YESSS