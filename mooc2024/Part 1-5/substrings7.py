
while True:
    input_string = input("Please type in a string: ")
    char = input("Now please type in a character you are looking for: ")

    position = 0

    t=0
    secondoc=0

    while True:
        t+=1
        i = input_string.find(char, position)
    
        if i == -1:  # no more occurrences
            break
   
        secondoc+=1
    
        if secondoc==2:
            second=i
            #print(secondoc)
        if t== 2: # only loop twice or look for twice
            break
    
        position = i + 1  # move past the last found index

    if secondoc==2:
        print(f"The second occurance '{char}' at index {second}")
    else:
        print(f"The substring does not occur twice in the string.")
        
