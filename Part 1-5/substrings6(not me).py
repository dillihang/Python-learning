while True:  # ← Outer loop: keeps asking the user for strings until they type "end"
    input_string = input("Please type in a string: ")  # ← Ask for a string
    if input_string == "end":  # ← If user typed "end", stop the program
        break

    char = input("Now please type in a character you are looking for: ")  # ← Ask for the character to search for

    temp_string = input_string  # ← Make a copy of the input string. We'll modify temp_string while searching
    while True:  # ← Inner loop: keep finding the character until no more occurrences
        i = temp_string.find(char)  # ← Find the first occurrence of `char` in temp_string
        if i == -1:  # ← If .find returns -1, char is not found → break inner loop
            break

        if i + 3 <= len(temp_string):  # ← Only print if there are at least 3 characters starting from i
            #print(i)
            print(f"found the {temp_string[i:i+3]}")  # ← Slice temp_string from i to i+3 and print
        #print(temp_string)
        temp_string = temp_string[i+1:]  # ← Remove everything up to and including this occurrence of char
                                          # ← This ensures next .find starts searching after the last found char
        