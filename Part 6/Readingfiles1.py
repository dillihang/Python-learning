def read_fruits():

    fruit_dict={}

    with open("Part 6/fruits.csv") as file:

        for line in file:
            
            line=line.replace("\n","")
            parts=line.split(";")

            fruits=parts[0]
            scores=parts[1:]

            for numbs in scores:

                fruit_dict[fruits]=float(numbs)
    
    print(fruit_dict)


read_fruits()

