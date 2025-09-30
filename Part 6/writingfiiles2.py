def filter_solutions():

    firstlist=[]
    fulllist=[]
    templist=[]
    # correctlist=[]
    # incorrectlist=[]

    with open("Part 6/correct.csv", "w") as new_file:
        pass

    with open("Part 6/incorrect.csv", "w") as my_file:
        pass

    with open("Part 6/solutions.csv") as file:

        for line in file:

            line=line.strip()
            part=line.split(";")
            firstlist.append(part)

            name=part[0]
            problem=part[1]
            result=int(part[2])
            my_list=[]
            
            my_list.append(problem)
            fulllist.append(my_list)

    
    for items in fulllist:
        for values in items:
            resultlist=[]
            if values[1]=="+":
               valuelist=values.split("+")
               value1=int(valuelist[0]) + int(valuelist[1])
            #    resultlist.append(values)
               resultlist.append(str(value1))
            else:
                valuelist=values.split("-")
                value2=int(valuelist[0]) - int(valuelist[1])
                # resultlist.append(values)
                resultlist.append(str(value2))
        templist.append(resultlist)


    for numbers in range(len(firstlist)):
        
        correctstring=""
        # tempstringlist=[]
        incorrectstring=""
        # tempincorrectstringlist=[]
        
        if templist[numbers][0]==firstlist[numbers][2]:
            correctstring+= firstlist[numbers][0]+";"
            correctstring+=firstlist[numbers][1]+";"
            correctstring+=firstlist[numbers][2]
            # tempstringlist.append(correctstring)
            with open("Part 6/correct.csv", "a") as new_file:

                new_file.write(f"{correctstring}\n")    
    
            
        else:

            incorrectstring+= firstlist[numbers][0]+";"
            incorrectstring+=firstlist[numbers][1]+";"
            incorrectstring+=firstlist[numbers][2]

            with open("Part 6/incorrect.csv", "a") as my_file:

                my_file.write(f"{incorrectstring}\n")



    #         tempincorrectstringlist.append(incorrectstring)

    #     if tempstringlist:
    #         correctlist.append(tempstringlist)

    #     if tempincorrectstringlist:
    #             incorrectlist.append(tempincorrectstringlist)    
           

    # print(correctlist)
    # print(incorrectlist)
        
            
filter_solutions()    
filter_solutions()
filter_solutions()
filter_solutions()
filter_solutions()
filter_solutions()
filter_solutions()

       
        

            
                    


               
            
            

           

    
                
                  
                    

                    








         








