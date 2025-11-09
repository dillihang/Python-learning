def filter_incorrect():

    new_list=[]
    my_list=[]


    alphabet=["abcdefghijklmnopqrstuvwxyz"]

    with open("Part 6/correct_numbers.csv", "a") as new_file:

        with open("Part 6/lottery_numbers.csv") as file:

            for line in file:
                line=line.strip()

                my_list.append(line)

                for items in alphabet:
                    for char in items:
                        
                        if char in line[5:]:
                            
                            new_list.append(line)

                                   
            for item in my_list[:]:

                if item in new_list or "*" in item:
                    my_list.remove(item)


            for titem in my_list[:]:

                newitem=titem.split(";")
                numbs=newitem[1]
                numbsplit=numbs.split(",")

                for bitems in numbsplit:

                    if int(bitems)<1 or int(bitems)>39:
                    
                        try:
                            my_list.remove(titem)

                        except ValueError:
                            pass

                    elif numbsplit.count(bitems)>1:
                        try:
                            my_list.remove(titem)

                        except ValueError:
                            pass
                            
                             
              
                if len(numbsplit) != 7: 
                    my_list.remove(titem)
            

            for lastitems in my_list:

                new_file.write(f"{lastitems}\n")                   

        


filter_incorrect()