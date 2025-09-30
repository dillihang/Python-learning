def return_int():

    numb_list=[]
    int_list=[]
    

    with open("Part 6/matrix.txt") as file:

        for line in file:
            
            line=line.replace("\n", "")
            parts=line.split(",")
            numbs=parts[0:]
            numb_list.append(numbs)

   
    for items in numb_list:
        for values in items:
            int_list.append(int(values))

    return int_list

 
def matrix_sum():    

    int_list=return_int()

    return (sum(int_list))

def matrix_max():
    
    int_list=return_int()

    return (max(int_list))       
            

def row_sums():

    int_list=return_int()

    finallist=[]


    finallist.append(sum(int_list[:12]))
    finallist.append((sum(int_list[12:])))

    return finallist




print(matrix_sum())
print(matrix_max())
print(row_sums())




