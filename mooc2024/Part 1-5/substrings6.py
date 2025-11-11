
while True:
    input_string = input("Please type in a string: ")
    if input_string=="end":
        break
    char = input("Now please type in a character you are looking for: ")

    

    temp_string=input_string

    t=0

    while t<=len(temp_string):

        i=temp_string.find(char)
        
        
        
               
        if i>=0:
            #print(temp_string)
            #print(i)
            if i+3<len(temp_string):
                print(temp_string[i:i+3])
            temp_string=temp_string[i+1:]    

            
            
            

            
            #print(i)
            #print(t)           
            
        t+=1
        #print(t)
        #print(temp_string)   
            #print(".")
            
        
        
        
        #YESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS FK YESSSSS

        
   
        
