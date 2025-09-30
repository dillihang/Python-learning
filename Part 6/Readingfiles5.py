line_list=[]
final_string=""

if True:
    
    string_list=input("Write text: ")

    string_list=string_list

    

    stringpart=string_list.split(" ")
   


    with open("Part 6/wordlist.txt") as file:

        for line in file:

            line=line.replace("\n", "")
            part=line.split(" ")

            for words in part:

                line_list.append(words.lower())

    print(line_list)


    for values in stringpart:
        if values.lower() in line_list:
            final_string+=values + " "
        
        else:
            final_string += f"*{values}*" + " "

    
    print(final_string)
