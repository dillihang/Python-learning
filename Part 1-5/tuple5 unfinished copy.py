def alphabet(alpha_dict: dict, alpha: str):

    for numb in range(1,(len(alpha)+1)):
        # print(f"{numb} : {alpha[numb-1]} ")

        alpha_dict[numb]=alpha[numb-1]
  

  
def printstars(alpha_dict: dict, times: int):

    
    mylist=[]

    print(f"Layers: {times}")
    height = times*2-1

    mynew_string=""

    mystring=alpha_dict[times]*height


    for index in range(height):
        
        if index==0:
            mylist.append(mystring)

        elif index==height-1:
            mylist.append(mystring)

        else:

            depth = min(index, height - 1 - index)

            row_string = ""

            for j in range(height):
                # figure out how far from edge this column is
                col_depth = min(j, height - 1 - j)
                
                # choose the "layer" = min(depth, col_depth)
                layer = min(depth, col_depth)
                
                # pick the letter for this layer
                row_string += alpha_dict[times - layer]

            mylist.append(row_string)
  

        
           
       
    
    # print(mylist)

    for numb in mylist:

        print(numb)
              
                


                
                

    
def main():
    alpha_dict={}

    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet(alpha_dict, alpha)

    printstars(alpha_dict, 4)
    # printstars(alpha_dict, 4)
    # printstars(alpha_dict, 26)
    print()

    # printstars(4)
    
    # print(alpha_dict)
    # print(alpha_dict[14])

main()



# rules are :

# if numb==5 length and height is 7
# each time the value of length increases the values of height changes
# so height goes for numb==4
# 7*char
# 4444444 * 7
# 4333334
# (0123456)	
# 4322234
# 4321234 Till it reachers 4 then the reverse or it increases chars in legth of each height
# 4322234
# 4333334
# 4444444