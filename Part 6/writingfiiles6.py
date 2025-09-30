# with open("Part 6/dictionary.txt", "w") as my_file:
#     pass

while True:

    print("1 - add word, 2 - search, 3 - quit")
    number=int(input("Function: "))
    
    if number==3:
        print("Bye!")
        break

    
    elif number==2:

        my_list=[]

        search_term=input("Search term: ")
        
        with open("Part 6/dictionary.txt") as file:
            
            for line in file:

                line=line.replace("\n", "")
                if search_term in line:
                    my_list.append(line)

        for items in my_list:
            print(items)
                    

    elif number==1:
        finnish=input("The word in Finnish: ")
        english=input("The word in English: ")

        with open("Part 6/dictionary.txt", "a") as my_file:

            my_file.write(f"{finnish} - ")
            my_file.write(f"{english}\n")
            print("Dictionary entry added")