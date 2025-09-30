while True:
    input_string = input("Please type in a string: ")
    char = input("Now please type in a character you are looking for: ")

    i=input_string.find(char)

    if input_string=="end":
        break

    if i>=0:
        c=i+3
        print(i)
        print(c)
        print(f"found the {input_string[i:c]}")
        
    else:
        print(f"not found")




   
    


    