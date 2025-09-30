test_content = """week 1;1,2,3,4,5,6,7
week zzc;1,5,13,22,24,25,26
week 2;9,13,14,24,34,35,37
week 3;1,*,5,6,13,2b,34
week 4;4,6,17,19,24,33
week 5;5,9,15,35,39,41,105
week 6;5,12,3,35,12,14,36
week 7;10,11,12,13,14,15,16
week 8;1,2,3,4,5,6,7
week 9a;1,2,3,4,5,6,7
week 10;1,1,2,3,4,5,6
week 11;0,1,2,3,4,5,6
week 12;1,2,3,4,5,6,40"""

with open("Part 6/lottery_numbers.csv", "w") as f:
    f.write(test_content)



def filter_incorrect():
    new_list=[]
    my_list=[]

    alphabet=["abcdefghijklmnopqrstuvwxyz"]

    with open("Part 6/correct_numbers copy.csv", "a") as new_file:
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

# Run it
filter_incorrect()

# Let's see the results
print("Input file:")
with open("Part 6/lottery_numbers.csv", "r") as f:
    print(f.read())

print("\nOutput file:")
with open("Part 6/correct_numbers.csv", "r") as f:
    print(f.read())